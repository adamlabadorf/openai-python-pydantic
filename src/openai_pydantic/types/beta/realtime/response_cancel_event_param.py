# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseCancelEventParam"]


class ResponseCancelEventParam(BaseModel):
    type: "Literal['response.cancel']"
    
    """The event type, must be `response.cancel`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""

    response_id: "Optional[str]"= None
    
    """
    A specific response ID to cancel - if not provided, will cancel an in-progress
    response in the default conversation.
    """
ResponseCancelEventParam.model_rebuild()

