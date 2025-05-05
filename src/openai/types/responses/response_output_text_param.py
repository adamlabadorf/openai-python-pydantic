# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = [
    "ResponseOutputTextParam",
    "Annotation",
    "AnnotationFileCitation",
    "AnnotationURLCitation",
    "AnnotationFilePath",
]


class AnnotationFileCitation(BaseModel):
    file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: str = None
    # old  file_id: Required[str]
    """The ID of the file."""

    index: Optional[int] = None
    # old  index: Optional[int] = None
    # old  index: Optional[int] = None
    # old  index: int = None
    # old  index: Required[int]
    """The index of the file in the list of files."""

    type: Optional[Literal["file_citation"]] = None
    # old  type: Optional[Literal["file_citation"]] = None
    # old  type: Optional[Literal["file_citation"]] = None
    # old  type: Literal["file_citation"] = None
    # old  type: Required[Literal["file_citation"]]
    """The type of the file citation. Always `file_citation`."""


class AnnotationURLCitation(BaseModel):
    end_index: Optional[int] = None
    # old  end_index: Optional[int] = None
    # old  end_index: Optional[int] = None
    # old  end_index: int = None
    # old  end_index: Required[int]
    """The index of the last character of the URL citation in the message."""

    start_index: Optional[int] = None
    # old  start_index: Optional[int] = None
    # old  start_index: Optional[int] = None
    # old  start_index: int = None
    # old  start_index: Required[int]
    """The index of the first character of the URL citation in the message."""

    title: Optional[str] = None
    # old  title: Optional[str] = None
    # old  title: Optional[str] = None
    # old  title: str = None
    # old  title: Required[str]
    """The title of the web resource."""

    type: Optional[Literal["url_citation"]] = None
    # old  type: Optional[Literal["url_citation"]] = None
    # old  type: Optional[Literal["url_citation"]] = None
    # old  type: Literal["url_citation"] = None
    # old  type: Required[Literal["url_citation"]]
    """The type of the URL citation. Always `url_citation`."""

    url: Optional[str] = None
    # old  url: Optional[str] = None
    # old  url: Optional[str] = None
    # old  url: str = None
    # old  url: Required[str]
    """The URL of the web resource."""


class AnnotationFilePath(BaseModel):
    file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: str = None
    # old  file_id: Required[str]
    """The ID of the file."""

    index: Optional[int] = None
    # old  index: Optional[int] = None
    # old  index: Optional[int] = None
    # old  index: int = None
    # old  index: Required[int]
    """The index of the file in the list of files."""

    type: Optional[Literal["file_path"]] = None
    # old  type: Optional[Literal["file_path"]] = None
    # old  type: Optional[Literal["file_path"]] = None
    # old  type: Literal["file_path"] = None
    # old  type: Required[Literal["file_path"]]
    """The type of the file path. Always `file_path`."""


Annotation = Union[AnnotationFileCitation, AnnotationURLCitation, AnnotationFilePath] # old Annotation: TypeAlias = Union[AnnotationFileCitation, AnnotationURLCitation, AnnotationFilePath]


class ResponseOutputTextParam(BaseModel):
    annotations: Optional[List[Annotation]] = None
    # old  annotations: Optional[List[Annotation]] = None
    # old  annotations: Optional[List[Annotation]] = None
    # old  annotations: List[Annotation] = None
    # old  annotations: Required[Iterable[Annotation]]
    """The annotations of the text output."""

    text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: str = None
    # old  text: Required[str]
    """The text output from the model."""

    type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Literal["output_text"] = None
    # old  type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""




