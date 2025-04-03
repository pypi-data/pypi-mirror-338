from .commons_pb2 import (
    InnerContextItem,
    ChatItem,
    ReplicaItem,
    OuterContextItem,
)
from .DigitalAssistantCritic_pb2_grpc import DigitalAssistantCriticStub
from .DigitalAssistantCritic_pb2 import (
    DigitalAssistantCriticRequest,
    DigitalAssistantCriticResponse,
)
from .abstract_client import AbstractClient


class CriticClient(AbstractClient):
    def __init__(self, address) -> None:
        super().__init__(address)
        self._stub = DigitalAssistantCriticStub(self._channel)

    def __call__(self, text: str, dict_chat: dict, request_id: str = "") -> str:

        dict_outer_context = dict_chat["OuterContext"]
        outer_context = OuterContextItem(
            Sex=dict_outer_context["Sex"],
            Age=dict_outer_context["Age"],
            UserId=dict_outer_context["UserId"],
            SessionId=dict_outer_context["SessionId"],
            ClientId=dict_outer_context["ClientId"],
            TrackId=dict_outer_context["TrackId"],
        )

        dict_inner_context = dict_chat["InnerContext"]
        dict_replicas = dict_inner_context["Replicas"]

        replicas = [
            ReplicaItem(
                Body=dict_replica["Body"],
                Role=dict_replica["Role"],
                DateTime=dict_replica["DateTime"],
            )
            for dict_replica in dict_replicas
        ]

        inner_context = InnerContextItem(Replicas=replicas)

        chat = ChatItem(OuterContext=outer_context, InnerContext=inner_context)

        request = DigitalAssistantCriticRequest(Text=text, Chat=chat, RequestId=request_id)

        response: DigitalAssistantCriticResponse = self._stub.GetCriticResponse(request)
        return response.Score
