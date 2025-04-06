from .commons_pb2 import OuterContextItem
from .DigitalAssistantMedVersaModels_pb2_grpc import DigitalAssistantMedVersaModelsStub
from .DigitalAssistantMedVersaModels_pb2 import (
    DigitalAssistantMedVersaModelsRequest,
    DigitalAssistantMedVersaModelsResponse,
)
from .abstract_client import AbstractClient


class MedVersaModelsClient(AbstractClient):
    def __init__(self, address):
        super().__init__(address)
        self._stub = DigitalAssistantMedVersaModelsStub(self._channel)

    def interpret(
        self,
        outer_context: OuterContextItem,
        resource_id: str,
        request_id: str = "",
    ) -> DigitalAssistantMedVersaModelsResponse:
        request = DigitalAssistantMedVersaModelsRequest(
            RequestId=request_id,
            OuterContext=outer_context,
            ResourceId=resource_id,
        )
        response: DigitalAssistantMedVersaModelsResponse = self._stub.Interpret(request)
        return response
