# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ConversationItemRetrieveEventParam"]


class ConversationItemRetrieveEventParam(BaseModel):
    item_id: str = None
    # old  item_id: Required[str]
    """The ID of the item to retrieve."""

    type: Literal["conversation.item.retrieve"] = None
    # old  type: Required[Literal["conversation.item.retrieve"]]
    """The event type, must be `conversation.item.retrieve`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

