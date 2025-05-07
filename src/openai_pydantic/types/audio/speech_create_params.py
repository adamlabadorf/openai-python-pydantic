# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

from .speech_model import SpeechModel

__all__ = ["SpeechCreateParams"]


class SpeechCreateParams(BaseModel):
    input: "str"
    
    """The text to generate audio for. The maximum length is 4096 characters."""

    model: "Union[str, SpeechModel]"
    
    """
    One of the available [TTS models](https://platform.openai.com/docs/models#tts):
    `tts-1`, `tts-1-hd` or `gpt-4o-mini-tts`.
    """

    voice: "Union[ str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'fable', 'onyx', 'nova', 'sage', 'shimmer', 'verse'] ]"
    
    """The voice to use when generating the audio.

    Supported voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`,
    `nova`, `sage`, `shimmer`, and `verse`. Previews of the voices are available in
    the
    [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).
    """

    instructions: "Optional[str]"= None
    
    """Control the voice of your generated audio with additional instructions.

    Does not work with `tts-1` or `tts-1-hd`.
    """

    response_format: "Optional[Literal['mp3', 'opus', 'aac', 'flac', 'wav', 'pcm']]"= None
    
    """The format to audio in.

    Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.
    """

    speed: "Optional[float]"= None
    
    """The speed of the generated audio.

    Select a value from `0.25` to `4.0`. `1.0` is the default. Does not work with
    `gpt-4o-mini-tts`.
    """
SpeechCreateParams.model_rebuild()

