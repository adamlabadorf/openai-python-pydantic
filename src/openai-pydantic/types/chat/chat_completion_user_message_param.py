# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .chat_completion_content_part_param import ChatCompletionContentPartParam

__all__ = ["ChatCompletionUserMessageParam"]


class ChatCompletionUserMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPartParam]] = None
    # old  content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The contents of the user message."""

    role: Literal["user"] = None
    # old  role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    name: Optional[str] = None
    # old  name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

