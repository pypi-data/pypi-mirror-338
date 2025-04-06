from agi_med_protos import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalAssistantMedVersaModelsRequest(_message.Message):
    __slots__ = ("RequestId", "OuterContext", "ResourceId")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    OUTERCONTEXT_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    RequestId: str
    OuterContext: _commons_pb2.OuterContextItem
    ResourceId: str
    def __init__(self, RequestId: _Optional[str] = ..., OuterContext: _Optional[_Union[_commons_pb2.OuterContextItem, _Mapping]] = ..., ResourceId: _Optional[str] = ...) -> None: ...

class DigitalAssistantMedVersaModelsResponse(_message.Message):
    __slots__ = ("ResourceId", "Disease", "DiseaseScore", "Description")
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    DISEASE_FIELD_NUMBER: _ClassVar[int]
    DISEASESCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ResourceId: str
    Disease: str
    DiseaseScore: float
    Description: str
    def __init__(self, ResourceId: _Optional[str] = ..., Disease: _Optional[str] = ..., DiseaseScore: _Optional[float] = ..., Description: _Optional[str] = ...) -> None: ...
