# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ConversationItemTruncateEventParam"]


class ConversationItemTruncateEventParam(BaseModel):
    audio_end_ms: int = None
    # old  audio_end_ms: Required[int]
    """Inclusive duration up to which audio is truncated, in milliseconds.

    If the audio_end_ms is greater than the actual audio duration, the server will
    respond with an error.
    """

    content_index: int = None
    # old  content_index: Required[int]
    """The index of the content part to truncate. Set this to 0."""

    item_id: str = None
    # old  item_id: Required[str]
    """The ID of the assistant message item to truncate.

    Only assistant message items can be truncated.
    """

    type: Literal["conversation.item.truncate"] = None
    # old  type: Required[Literal["conversation.item.truncate"]]
    """The event type, must be `conversation.item.truncate`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

