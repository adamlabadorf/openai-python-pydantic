# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["ResponseReasoningItemParam", "Summary"]


class Summary(BaseModel):
    text: "str"
    
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: "Literal['summary_text']"
    
    """The type of the object. Always `summary_text`."""


class ResponseReasoningItemParam(BaseModel):
    id: "str"
    
    """The unique identifier of the reasoning content."""

    summary: "List[Summary]"
    
    """Reasoning text contents."""

    type: "Literal['reasoning']"
    
    """The type of the object. Always `reasoning`."""

    encrypted_content: "Optional[str]"= None
    
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: "Optional[Literal['in_progress', 'completed', 'incomplete']]"= None
    
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """
Summary.model_rebuild()
ResponseReasoningItemParam.model_rebuild()

