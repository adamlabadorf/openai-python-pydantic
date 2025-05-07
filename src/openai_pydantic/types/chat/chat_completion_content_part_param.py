# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
from .chat_completion_content_part_input_audio_param import ChatCompletionContentPartInputAudioParam

__all__ = ["ChatCompletionContentPartParam", "File", "FileFile"]


class FileFile(BaseModel):
    file_data: "Optional[str]"= None
    
    """
    The base64 encoded file data, used when passing the file to the model as a
    string.
    """

    file_id: "Optional[str]"= None
    
    """The ID of an uploaded file to use as input."""

    filename: "Optional[str]"= None
    
    """The name of the file, used when passing the file to the model as a string."""


class File(BaseModel):
    file: "FileFile"
    

    type: "Literal['file']"
    
    """The type of the content part. Always `file`."""


ChatCompletionContentPartParam = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartInputAudioParam,
    File,
]
FileFile.model_rebuild()
File.model_rebuild()

