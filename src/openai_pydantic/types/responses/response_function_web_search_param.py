# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseFunctionWebSearchParam"]


class ResponseFunctionWebSearchParam(BaseModel):
    id: "str"
    
    """The unique ID of the web search tool call."""

    status: "Literal['in_progress', 'searching', 'completed', 'failed']"
    
    """The status of the web search tool call."""

    type: "Literal['web_search_call']"
    
    """The type of the web search tool call. Always `web_search_call`."""
ResponseFunctionWebSearchParam.model_rebuild()

