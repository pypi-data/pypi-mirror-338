from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DocType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PDF: _ClassVar[DocType]
    JPG: _ClassVar[DocType]
    PNG: _ClassVar[DocType]
    PDF_SCAN: _ClassVar[DocType]

class OCRType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEXT_ONLY: _ClassVar[OCRType]
    TEXT_WITH_TABLES: _ClassVar[OCRType]
    TEXT_WITH_IMAGES: _ClassVar[OCRType]
    TEXT_WITH_TABLES_AND_IMAGES: _ClassVar[OCRType]
PDF: DocType
JPG: DocType
PNG: DocType
PDF_SCAN: DocType
TEXT_ONLY: OCRType
TEXT_WITH_TABLES: OCRType
TEXT_WITH_IMAGES: OCRType
TEXT_WITH_TABLES_AND_IMAGES: OCRType

class DigitalAssistantOCRRequest(_message.Message):
    __slots__ = ("Document", "Type", "RequestId", "OCRType")
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    OCRTYPE_FIELD_NUMBER: _ClassVar[int]
    Document: bytes
    Type: DocType
    RequestId: str
    OCRType: OCRType
    def __init__(self, Document: _Optional[bytes] = ..., Type: _Optional[_Union[DocType, str]] = ..., RequestId: _Optional[str] = ..., OCRType: _Optional[_Union[OCRType, str]] = ...) -> None: ...

class DigitalAssistantOCRResponse(_message.Message):
    __slots__ = ("Text", "StructuredResourceId")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    STRUCTUREDRESOURCEID_FIELD_NUMBER: _ClassVar[int]
    Text: str
    StructuredResourceId: str
    def __init__(self, Text: _Optional[str] = ..., StructuredResourceId: _Optional[str] = ...) -> None: ...
