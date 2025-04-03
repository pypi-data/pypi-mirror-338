from typing import Tuple

from .DigitalAssistantContentRouter_pb2_grpc import DigitalAssistantContentRouterStub
from .DigitalAssistantContentRouter_pb2 import (
    DigitalAssistantContentRouterRequest,
    DigitalAssistantContentRouterResponse,
)
from .abstract_client import AbstractClient


ResourceId = str
Interpretation = str

class ContentRouterClient(AbstractClient):
    def __init__(self, address):
        super().__init__(address)
        self._stub = DigitalAssistantContentRouterStub(self._channel)

    def __call__(
        self, resource_id: str, prompt: str, request_id: str = ""
    ) -> Tuple[ResourceId, Interpretation]:
        request = DigitalAssistantContentRouterRequest(
            RequestId=request_id,
            ResourceId=resource_id,
            Prompt=prompt,
        )
        response: DigitalAssistantContentRouterResponse = self._stub.Interpret(request)
        return response.ResourceId, response.Interpretation
