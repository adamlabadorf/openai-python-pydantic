# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionAudioParam"]


class ChatCompletionAudioParam(BaseModel):
    format: Literal["wav", "aac", "mp3", "flac", "opus", "pcm16"] = None
    # old  format: Required[Literal["wav", "aac", "mp3", "flac", "opus", "pcm16"]]
    """Specifies the output audio format.

    Must be one of `wav`, `mp3`, `flac`, `opus`, or `pcm16`.
    """

    voice:  Union[ str, Literal["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer", "verse" ] ] = None
    # old  voice: Required[ Union[ str, Literal["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer", "verse"] ] ]
    """The voice the model uses to respond.

    Supported voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`,
    `onyx`, `sage`, and `shimmer`.
    """

