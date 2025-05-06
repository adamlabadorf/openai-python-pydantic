# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ConversationItemContentParam"]


class ConversationItemContentParam(BaseModel):
    id: "Optional[str]"= None
    
    """
    ID of a previous conversation item to reference (for `item_reference` content
    types in `response.create` events). These can reference both client and server
    created items.
    """

    audio: "Optional[str]"= None
    
    """Base64-encoded audio bytes, used for `input_audio` content type."""

    text: "Optional[str]"= None
    
    """The text content, used for `input_text` and `text` content types."""

    transcript: "Optional[str]"= None
    
    """The transcript of the audio, used for `input_audio` content type."""

    type: "Optional[Literal['input_text', 'input_audio', 'item_reference', 'text']]"= None
    
    """The content type (`input_text`, `input_audio`, `item_reference`, `text`)."""
ConversationItemContentParam.model_rebuild()

