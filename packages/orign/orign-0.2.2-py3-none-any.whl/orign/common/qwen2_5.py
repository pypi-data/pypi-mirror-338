import os
from typing import Dict, List, Optional

from nebu.containers.container import Container
from nebu.containers.models import (
    V1ContainerRequest,
    V1ContainerSearch,
    V1EnvVar,
    V1Meter,
    V1ResourceMetaRequest,
    V1VolumeDriver,
    V1VolumePath,
)
from pydantic import BaseModel

from orign.buffers.models import V1ReplayBufferRequest
from orign.config import GlobalConfig
from orign.llms.llm import OnlineLLM


class VLLMOpts(BaseModel):
    accelerators: List[str]
    gpu_memory_utilization: float = 0.8
    max_num_seqs: int = 1
    dtype: str = "bfloat16"
    price_per_token: Optional[float] = None
    platform: Optional[str] = None
    shared: bool = False


class TRLOpts(BaseModel):
    accelerators: List[str]
    train_type: str = "sft"
    num_train_epochs: int = 1
    save_steps: int = 1
    save_total_limit: int = 3
    save_strategy: str = "steps"
    dtype: str = "bfloat16"
    per_device_train_batch_size: int = 1
    per_device_eval_batch_size: int = 1
    output_dir: str = "/output"
    price_per_training_second: Optional[float] = None
    platform: Optional[str] = None


class Qwen2_5(OnlineLLM):
    def __init__(
        self,
        name: str,
        model: str,
        platform: str,
        bucket: str,
        train_opts: TRLOpts,
        infer_opts: VLLMOpts,
        lora: bool = True,
        namespace: str = "default",
        train_every: int = 50,
        sample_n: int = 100,
        sample_strategy: str = "Random",
        use_peft: bool = True,
        max_seq_length: int = 2048,
        timeout: str = "2h",
        bucket_base_key: str = "orign",
        labels: Optional[Dict[str, str]] = None,
        config: Optional[GlobalConfig] = None,
    ):
        self.model = model
        self.platform = platform
        self.train_opts = train_opts
        self.infer_opts = infer_opts
        self.lora = lora

        train_platform = train_opts.platform or platform

        train_command = f"""
source activate trl && trl {train_opts.train_type} \
    --model_name_or_path $MODEL \
    --dataset_name $DATASET_PATH \
    --dataset_train_split "train" \
    --dataset_test_split "test" \
    --output_dir {train_opts.output_dir}/{namespace}/{name}/jobs/$NEBU_CONTAINER_ID \
    --torch_dtype {train_opts.dtype} \
    --max_seq_length {max_seq_length} \
    --per_device_train_batch_size {train_opts.per_device_train_batch_size} \
    --per_device_eval_batch_size {train_opts.per_device_eval_batch_size} \
    --use_peft {use_peft} \
    --save_strategy {train_opts.save_strategy} \
    --save_steps {train_opts.save_steps} \
    --save_total_limit {train_opts.save_total_limit} \
    --num_train_epochs {train_opts.num_train_epochs}
LATEST="$(ls -1d {train_opts.output_dir}/{namespace}/{name}/jobs/$NEBU_CONTAINER_ID/checkpoint-* | sort -V | tail -n 1)"
rclone sync "$LATEST" "s3://{bucket}/{bucket_base_key}/{namespace}/{name}/latest"
        """

        train_meters = None
        if train_opts.price_per_training_second:
            train_meters = [
                V1Meter(
                    cost=train_opts.price_per_training_second,
                    unit="second",
                    metric="runtime",
                    currency="USD",
                )
            ]

        train_queue_name = f"trl-{name}"

        train_env = [
            V1EnvVar(key="MODEL", value=model),
        ]

        if os.getenv("HF_TOKEN"):
            train_env.append(V1EnvVar(key="HF_TOKEN", value=os.getenv("HF_TOKEN")))

        train_volumes = [
            V1VolumePath(
                source=f"{train_opts.output_dir}/{namespace}/{name}/jobs/$NEBU_CONTAINER_ID",
                dest=f"s3://{bucket}/{bucket_base_key}/{namespace}/{name}/jobs/$NEBU_CONTAINER_ID",
                driver=V1VolumeDriver.RCLONE_SYNC,
                continuous=True,
            )
        ]

        self.train_job = V1ContainerRequest(
            image="huggingface/trl-latest-gpu:latest",
            platform=train_platform,
            metadata=V1ResourceMetaRequest(
                name=f"{name}-trl",
                namespace=namespace,
                labels=labels,
            ),
            command=train_command,
            accelerators=train_opts.accelerators,
            env=train_env,
            volumes=train_volumes,
            meters=train_meters,
            restart="Never",
            queue=train_queue_name,
            timeout=timeout,
        )

        self.replay_buffer = V1ReplayBufferRequest(
            metadata=V1ResourceMetaRequest(
                name=f"{name}-buffer",
                namespace=namespace,
                labels=labels,
            ),
            sample_n=sample_n,
            sample_strategy=sample_strategy,
            train_every=train_every,
            num_epochs=train_opts.num_train_epochs,
            train_job=self.train_job,
        )

        self.server = None
        if infer_opts.shared:
            params = V1ContainerSearch(
                namespace=namespace,
                accelerators=infer_opts.accelerators,
                platform=infer_opts.platform,
                env=self._create_vllm_env(model, lora),
                command=self._create_vllm_command(infer_opts, max_seq_length, lora),
                proxy_port=8000,
                meters=self._create_vllm_meters(infer_opts.price_per_token),
                restart="Always",
            )
            containers = Container.search(params)
            if len(containers) != 0:
                print(
                    f"Found existing vLLM server to share for Qwen2.5: {containers[0].metadata.name}"
                )
                server = Container.from_v1(containers[0])
                self.server = server.ref()

        if not self.server:
            self.config = config or GlobalConfig.read()
            self.api_key = self.config.api_key
            self.orign_host = self.config.server
            self.llms_url = f"{self.orign_host}/v1/llms"

            inference_platform = infer_opts.platform or platform
            inference_volumes = [
                V1VolumePath(
                    source=f"s3://{bucket}/{bucket_base_key}",
                    dest="/adapters",
                    driver=V1VolumeDriver.RCLONE_SYNC,
                    continuous=True,
                )
            ]

            self.server = V1ContainerRequest(
                metadata=V1ResourceMetaRequest(
                    name=f"{name}-vllm",
                    namespace=namespace,
                    labels=labels,
                ),
                image="vllm/vllm-openai:latest",
                platform=inference_platform,
                accelerators=infer_opts.accelerators,
                env=self._create_vllm_env(model, lora),
                command=self._create_vllm_command(infer_opts, max_seq_length, lora),
                volumes=inference_volumes,
                restart="Always",
                proxy_port=8000,
                meters=self._create_vllm_meters(infer_opts.price_per_token),
            )

        super().__init__(
            name=name,
            model=model,
            namespace=namespace,
            labels=labels,
            server=self.server,
            buffer=self.replay_buffer,
        )

    def _create_vllm_command(
        self, infer_opts: VLLMOpts, max_seq_length: int, lora: bool = False
    ) -> str:
        command = f"""python3 -m vllm.entrypoints.openai.api_server \
            --model $MODEL \
            --port 8000 \
            --host 0.0.0.0 \
            --gpu-memory-utilization {infer_opts.gpu_memory_utilization} \
            --max-model-len {max_seq_length} \
            --max-num-seqs {infer_opts.max_num_seqs} \
            --dtype {infer_opts.dtype}"""

        if lora:
            command += " --enable-lora"
        return command

    def _create_vllm_env(self, model: str, lora: bool = False) -> List[V1EnvVar]:
        env = [V1EnvVar(key="MODEL", value=model)]

        if os.getenv("HF_TOKEN"):
            env.append(V1EnvVar(key="HF_TOKEN", value=os.getenv("HF_TOKEN")))
        if lora:
            env.append(V1EnvVar(key="VLLM_ALLOW_RUNTIME_LORA_UPDATING", value="True"))

        return env

    def _create_vllm_meters(
        self, price_per_token: Optional[float]
    ) -> Optional[List[V1Meter]]:
        if not price_per_token:
            return None

        return [
            V1Meter(
                cost=price_per_token,
                unit="token",
                metric="response_value",
                json_path="$.usage.completion_tokens",
                currency="USD",
            )
        ]
