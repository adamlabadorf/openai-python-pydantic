# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseFunctionWebSearchParam"]


class ResponseFunctionWebSearchParam(BaseModel):
    id: str = None
    # old  id: Required[str]
    """The unique ID of the web search tool call."""

    status: Literal["in_progress", "searching", "completed", "failed"] = None
    # old  status: Required[Literal["in_progress", "searching", "completed", "failed"]]
    """The status of the web search tool call."""

    type: Literal["web_search_call"] = None
    # old  type: Required[Literal["web_search_call"]]
    """The type of the web search tool call. Always `web_search_call`."""

