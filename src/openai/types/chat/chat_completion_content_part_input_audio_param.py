# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionContentPartInputAudioParam", "InputAudio"]


class InputAudio(BaseModel):
    data: Optional[str] = None
    # old  data: str = None
    # old  data: Required[str]
    """Base64 encoded audio data."""

    format: Optional[Literal["wav", "mp3"]] = None
    # old  format: Literal["wav", "mp3"] = None
    # old  format: Required[Literal["wav", "mp3"]]
    """The format of the encoded audio data. Currently supports "wav" and "mp3"."""


class ChatCompletionContentPartInputAudioParam(BaseModel):
    input_audio: Optional[InputAudio] = None
    # old  input_audio: InputAudio = None
    # old  input_audio: Required[InputAudio]

    type: Optional[Literal["input_audio"]] = None
    # old  type: Literal["input_audio"] = None
    # old  type: Required[Literal["input_audio"]]
    """The type of the content part. Always `input_audio`."""


