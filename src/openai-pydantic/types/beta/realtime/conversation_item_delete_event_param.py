# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ConversationItemDeleteEventParam"]


class ConversationItemDeleteEventParam(BaseModel):
    item_id: str = None
    # old  item_id: Required[str]
    """The ID of the item to delete."""

    type: Literal["conversation.item.delete"] = None
    # old  type: Required[Literal["conversation.item.delete"]]
    """The event type, must be `conversation.item.delete`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

