from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ("Text", "Tables", "Images")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    Text: str
    Tables: _containers.RepeatedCompositeFieldContainer[Table]
    Images: _containers.RepeatedCompositeFieldContainer[Image]
    def __init__(self, Text: _Optional[str] = ..., Tables: _Optional[_Iterable[_Union[Table, _Mapping]]] = ..., Images: _Optional[_Iterable[_Union[Image, _Mapping]]] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ("Page", "TableMD", "Description", "Caption")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TABLEMD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    Page: int
    TableMD: str
    Description: str
    Caption: str
    def __init__(self, Page: _Optional[int] = ..., TableMD: _Optional[str] = ..., Description: _Optional[str] = ..., Caption: _Optional[str] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("Page", "Description", "Caption")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    Page: int
    Description: str
    Caption: str
    def __init__(self, Page: _Optional[int] = ..., Description: _Optional[str] = ..., Caption: _Optional[str] = ...) -> None: ...
