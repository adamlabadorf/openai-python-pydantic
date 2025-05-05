# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["InputAudioBufferAppendEventParam"]


class InputAudioBufferAppendEventParam(BaseModel):
    audio: str = None
    # old  audio: Required[str]
    """Base64-encoded audio bytes.

    This must be in the format specified by the `input_audio_format` field in the
    session configuration.
    """

    type: Literal["input_audio_buffer.append"] = None
    # old  type: Required[Literal["input_audio_buffer.append"]]
    """The event type, must be `input_audio_buffer.append`."""

    event_id: Optional[str] = None
    # old  event_id: str
    """Optional client-generated ID used to identify this event."""

