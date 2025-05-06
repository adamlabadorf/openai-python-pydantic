# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

from .response_output_text_param import ResponseOutputTextParam
from .response_output_refusal_param import ResponseOutputRefusalParam

__all__ = ["ResponseOutputMessageParam", "Content"]

Content = Union[ResponseOutputTextParam, ResponseOutputRefusalParam]


class ResponseOutputMessageParam(BaseModel):
    id: "str"= None
    
    """The unique ID of the output message."""

    content: "List[Content]"= None
    
    """The content of the output message."""

    role: "Literal['assistant']"= None
    
    """The role of the output message. Always `assistant`."""

    status: "Literal['in_progress', 'completed', 'incomplete']"= None
    
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: "Literal['message']"= None
    
    """The type of the output message. Always `message`."""
ResponseOutputMessageParam.model_rebuild()

