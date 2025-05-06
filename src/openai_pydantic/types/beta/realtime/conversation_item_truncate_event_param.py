# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ConversationItemTruncateEventParam"]


class ConversationItemTruncateEventParam(BaseModel):
    audio_end_ms: "int"= None
    
    """Inclusive duration up to which audio is truncated, in milliseconds.

    If the audio_end_ms is greater than the actual audio duration, the server will
    respond with an error.
    """

    content_index: "int"= None
    
    """The index of the content part to truncate. Set this to 0."""

    item_id: "str"= None
    
    """The ID of the assistant message item to truncate.

    Only assistant message items can be truncated.
    """

    type: "Literal['conversation.item.truncate']"= None
    
    """The event type, must be `conversation.item.truncate`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""
ConversationItemTruncateEventParam.model_rebuild()

