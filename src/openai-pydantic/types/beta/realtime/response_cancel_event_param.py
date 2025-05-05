# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseCancelEventParam"]


class ResponseCancelEventParam(BaseModel):
    type: Literal["response.cancel"] = None
    # old  type: Required[Literal["response.cancel"]]
    """The event type, must be `response.cancel`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

    response_id: Optional[str] = None
    # old  response_id: str
    """
    A specific response ID to cancel - if not provided, will cancel an in-progress
    response in the default conversation.
    """

