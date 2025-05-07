# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["InputAudioBufferCommitEventParam"]


class InputAudioBufferCommitEventParam(BaseModel):
    type: "Literal['input_audio_buffer.commit']"
    
    """The event type, must be `input_audio_buffer.commit`."""

    event_id: "Optional[str]"= None
    
    """Optional client-generated ID used to identify this event."""
InputAudioBufferCommitEventParam.model_rebuild()

