# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseReasoningItemParam", "Summary"]


class Summary(BaseModel):
    text: Optional[str] = None
    # old  text: str = None
    # old  text: Required[str]
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: Optional[Literal["summary_text"]] = None
    # old  type: Literal["summary_text"] = None
    # old  type: Required[Literal["summary_text"]]
    """The type of the object. Always `summary_text`."""


class ResponseReasoningItemParam(BaseModel):
    id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The unique identifier of the reasoning content."""

    summary: Optional[List[Summary]] = None
    # old  summary: List[Summary] = None
    # old  summary: Required[Iterable[Summary]]
    """Reasoning text contents."""

    type: Optional[Literal["reasoning"]] = None
    # old  type: Literal["reasoning"] = None
    # old  type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""

    encrypted_content: Optional[str] = None
    # old  encrypted_content: Optional[str] = None
    # old  encrypted_content: Optional[str]
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


