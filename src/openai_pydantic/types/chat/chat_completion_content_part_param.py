# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal
from pydantic import BaseModel
from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
from .chat_completion_content_part_input_audio_param import ChatCompletionContentPartInputAudioParam

__all__ = ["ChatCompletionContentPartParam", "File", "FileFile"]


class FileFile(BaseModel):
    file_data: Optional[str] = None
    # old  file_data: Optional[str] = None
    # old  file_data: str
    """
    The base64 encoded file data, used when passing the file to the model as a
    string.
    """

    file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: str
    """The ID of an uploaded file to use as input."""

    filename: Optional[str] = None
    # old  filename: Optional[str] = None
    # old  filename: str
    """The name of the file, used when passing the file to the model as a string."""


class File(BaseModel):
    file: Optional[FileFile] = None
    # old  file: FileFile = None
    # old  file: Required[FileFile]

    type: Optional[Literal["file"]] = None
    # old  type: Literal["file"] = None
    # old  type: Required[Literal["file"]]
    """The type of the content part. Always `file`."""


ChatCompletionContentPartParam = Union[ # old ChatCompletionContentPartParam: TypeAlias = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartInputAudioParam,
    File,
]


