# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ConversationItemRetrieveEventParam"]


class ConversationItemRetrieveEventParam(BaseModel):
    item_id: "str"= None
    
    """The ID of the item to retrieve."""

    type: "Literal['conversation.item.retrieve']"= None
    
    """The event type, must be `conversation.item.retrieve`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""
ConversationItemRetrieveEventParam.model_rebuild()

