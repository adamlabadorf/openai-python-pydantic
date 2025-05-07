# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ChatCompletionContentPartInputAudioParam", "InputAudio"]


class InputAudio(BaseModel):
    data: "str"
    
    """Base64 encoded audio data."""

    format: "Literal['wav', 'mp3']"
    
    """The format of the encoded audio data. Currently supports "wav" and "mp3"."""


class ChatCompletionContentPartInputAudioParam(BaseModel):
    input_audio: "InputAudio"
    

    type: "Literal['input_audio']"
    
    """The type of the content part. Always `input_audio`."""
InputAudio.model_rebuild()
ChatCompletionContentPartInputAudioParam.model_rebuild()

