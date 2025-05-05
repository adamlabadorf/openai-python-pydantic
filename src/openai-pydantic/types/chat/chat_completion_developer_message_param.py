# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionDeveloperMessageParam"]


class ChatCompletionDeveloperMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPartTextParam]] = None
    # old  content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]
    """The contents of the developer message."""

    role: Literal["developer"] = None
    # old  role: Required[Literal["developer"]]
    """The role of the messages author, in this case `developer`."""

    name: Optional[str] = None
    # old  name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

