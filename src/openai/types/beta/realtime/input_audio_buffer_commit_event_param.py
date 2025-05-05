# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["InputAudioBufferCommitEventParam"]


class InputAudioBufferCommitEventParam(BaseModel):
    type: Literal["input_audio_buffer.commit"] = None
    # old  type: Required[Literal["input_audio_buffer.commit"]]
    """The event type, must be `input_audio_buffer.commit`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

