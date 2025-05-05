# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .response_output_text_param import ResponseOutputTextParam
from .response_output_refusal_param import ResponseOutputRefusalParam

__all__ = ["ResponseOutputMessageParam", "Content"]

Content = Union[ResponseOutputTextParam, ResponseOutputRefusalParam] # old Content: TypeAlias = Union[ResponseOutputTextParam, ResponseOutputRefusalParam]


class ResponseOutputMessageParam(BaseModel):
    id: str = None
    # old  id: Required[str]
    """The unique ID of the output message."""

    content: List[Content] = None
    # old  content: Required[Iterable[Content]]
    """The content of the output message."""

    role: Literal["assistant"] = None
    # old  role: Required[Literal["assistant"]]
    """The role of the output message. Always `assistant`."""

    status: Literal["in_progress", "completed", "incomplete"] = None
    # old  status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: Literal["message"] = None
    # old  type: Required[Literal["message"]]
    """The type of the output message. Always `message`."""

