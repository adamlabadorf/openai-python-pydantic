# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

__all__ = ["ChatCompletionAudioParam"]


class ChatCompletionAudioParam(BaseModel):
    format: "Literal['wav', 'aac', 'mp3', 'flac', 'opus', 'pcm16']"
    
    """Specifies the output audio format.

    Must be one of `wav`, `mp3`, `flac`, `opus`, or `pcm16`.
    """

    voice: "Union[ str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'fable', 'onyx', 'nova', 'sage', 'shimmer', 'verse'] ]"
    
    """The voice the model uses to respond.

    Supported voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`,
    `onyx`, `sage`, and `shimmer`.
    """
ChatCompletionAudioParam.model_rebuild()

