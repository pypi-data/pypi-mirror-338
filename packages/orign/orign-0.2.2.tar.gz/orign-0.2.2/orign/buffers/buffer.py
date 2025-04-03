from typing import Dict, List, Optional

import requests

from orign.buffers.models import (
    V1ContainerRequest,
    V1ReplayBuffer,
    V1ReplayBufferData,
    V1ReplayBufferRequest,
    V1ReplayBuffersResponse,
    V1ResourceMetaRequest,
    V1UpdateReplayBufferRequest,
)
from orign.config import GlobalConfig


class ReplayBuffer:
    def __init__(
        self,
        name: str,
        train_job: V1ContainerRequest,
        namespace: str = "default",
        train_every: int = 50,
        sample_n: int = 100,
        sample_strategy: str = "Random",
        labels: Optional[Dict[str, str]] = None,
        config: Optional[GlobalConfig] = None,
    ):
        config = config or GlobalConfig.read()
        self.api_key = config.api_key
        self.orign_host = config.server

        # Construct the WebSocket URL with query parameters
        self.buffers_url = f"{self.orign_host}/v1/buffers"

        response = requests.get(
            self.buffers_url, headers={"Authorization": f"Bearer {self.api_key}"}
        )
        response.raise_for_status()
        buffers = V1ReplayBuffersResponse.model_validate(response.json())
        self.buffer = next(
            (
                b
                for b in buffers.buffers
                if b.metadata.name == name and b.metadata.namespace == namespace
            ),
            None,
        )

        if not self.buffer:
            request = V1ReplayBufferRequest(
                metadata=V1ResourceMetaRequest(
                    name=name,
                    namespace=namespace,
                    labels=labels,
                ),
                train_every=train_every,
                sample_n=sample_n,
                sample_strategy=sample_strategy,
                train_job=train_job,
            )
            response = requests.post(
                self.buffers_url,
                json=request.model_dump(),
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            self.buffer = V1ReplayBuffer.model_validate(response.json())
            print(f"Created buffer {self.buffer.metadata.name}")
        else:
            print(f"Found buffer {self.buffer.metadata.name}, updating if necessary")
            request = V1UpdateReplayBufferRequest(
                train_every=train_every,
                sample_n=sample_n,
                sample_strategy=sample_strategy,
                train_job=train_job,
            )
            response = requests.patch(
                f"{self.buffers_url}/{self.buffer.metadata.namespace}/{self.buffer.metadata.name}",
                json=request.model_dump(),
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            print(f"Updated buffer {self.buffer.metadata.name}")

    def send(self, data: List[dict], train: Optional[bool] = None):
        if not self.buffer or not self.buffer.metadata.name:
            raise ValueError("Buffer not found")

        url = f"{self.buffers_url}/{self.buffer.metadata.namespace}/{self.buffer.metadata.name}/examples"

        request = V1ReplayBufferData(examples=data, train=train)

        response = requests.post(
            url,
            json=request.model_dump(),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        response.raise_for_status()
        return response.json()

    def train(self):
        if not self.buffer or not self.buffer.metadata.name:
            raise ValueError("Buffer not found")

        url = f"{self.buffers_url}/{self.buffer.metadata.namespace}/{self.buffer.metadata.name}/train"
        response = requests.post(
            url, headers={"Authorization": f"Bearer {self.api_key}"}
        )
        response.raise_for_status()
        return response.json()

    @classmethod
    def get(
        cls,
        namespace: Optional[str] = None,
        name: Optional[str] = None,
        config: Optional[GlobalConfig] = None,
    ) -> List[V1ReplayBuffer]:
        config = config or GlobalConfig.read()

        # Construct the WebSocket URL with query parameters
        buffers_url = f"{config.server}/v1/buffers"

        response = requests.get(
            buffers_url, headers={"Authorization": f"Bearer {config.api_key}"}
        )
        response.raise_for_status()
        buffer_response = V1ReplayBuffersResponse.model_validate(response.json())
        buffers = buffer_response.buffers
        if name:
            buffers = [b for b in buffers if b.metadata.name == name]

        if namespace:
            buffers = [b for b in buffers if b.metadata.namespace == namespace]

        return buffers
