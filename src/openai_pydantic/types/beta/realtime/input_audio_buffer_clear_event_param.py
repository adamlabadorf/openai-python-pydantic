# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["InputAudioBufferClearEventParam"]


class InputAudioBufferClearEventParam(BaseModel):
    type: "Literal['input_audio_buffer.clear']"= None
    
    """The event type, must be `input_audio_buffer.clear`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""
InputAudioBufferClearEventParam.model_rebuild()

