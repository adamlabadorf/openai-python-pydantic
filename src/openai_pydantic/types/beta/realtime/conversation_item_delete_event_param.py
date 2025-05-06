# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ConversationItemDeleteEventParam"]


class ConversationItemDeleteEventParam(BaseModel):
    item_id: "str"= None
    
    """The ID of the item to delete."""

    type: "Literal['conversation.item.delete']"= None
    
    """The event type, must be `conversation.item.delete`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""
ConversationItemDeleteEventParam.model_rebuild()

