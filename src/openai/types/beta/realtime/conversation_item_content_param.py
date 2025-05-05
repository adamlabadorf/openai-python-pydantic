# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ConversationItemContentParam"]


class ConversationItemContentParam(BaseModel):
    id: Optional[str] = None
    # old  id: str
    """
    ID of a previous conversation item to reference (for `item_reference` content
    types in `response.create` events). These can reference both client and server
    created items.
    """

    audio: Optional[str] = None
    # old  audio: str
    """Base64-encoded audio bytes, used for `input_audio` content type."""

    text: Optional[str] = None
    # old  text: str
    """The text content, used for `input_text` and `text` content types."""

    transcript: Optional[str] = None
    # old  transcript: str
    """The transcript of the audio, used for `input_audio` content type."""

    type: Optional[Literal["input_text", "input_audio", "item_reference", "text"]] = None
    # old  type: Literal["input_text", "input_audio", "item_reference", "text"]
    """The content type (`input_text`, `input_audio`, `item_reference`, `text`)."""

