from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalAssistantContentRouterRequest(_message.Message):
    __slots__ = ("RequestId", "ResourceId", "Prompt")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    RequestId: str
    ResourceId: str
    Prompt: str
    def __init__(self, RequestId: _Optional[str] = ..., ResourceId: _Optional[str] = ..., Prompt: _Optional[str] = ...) -> None: ...

class DigitalAssistantContentRouterResponse(_message.Message):
    __slots__ = ("Interpretation", "ResourceId")
    INTERPRETATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    Interpretation: str
    ResourceId: str
    def __init__(self, Interpretation: _Optional[str] = ..., ResourceId: _Optional[str] = ...) -> None: ...
