# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = [
    "CreateEvalJSONLRunDataSourceParam",
    "Source",
    "SourceFileContent",
    "SourceFileContentContent",
    "SourceFileID",
]


class SourceFileContentContent(BaseModel):
    item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Dict[str, object] = None
    # old  item: Required[Dict[str, object]]

    sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Dict[str, object]


class SourceFileContent(BaseModel):
    content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: List[SourceFileContentContent] = None
    # old  content: Required[Iterable[SourceFileContentContent]]
    """The content of the jsonl file."""

    type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Literal["file_content"] = None
    # old  type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class SourceFileID(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The identifier of the file."""

    type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Literal["file_id"] = None
    # old  type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


Source = Union[SourceFileContent, SourceFileID] # old Source: TypeAlias = Union[SourceFileContent, SourceFileID]


class CreateEvalJSONLRunDataSourceParam(BaseModel):
    source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Source = None
    # old  source: Required[Source]

    type: Optional[Literal["jsonl"]] = None
    # old  type: Optional[Literal["jsonl"]] = None
    # old  type: Optional[Literal["jsonl"]] = None
    # old  type: Literal["jsonl"] = None
    # old  type: Required[Literal["jsonl"]]
    """The type of data source. Always `jsonl`."""




