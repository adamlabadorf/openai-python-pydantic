# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionToolMessageParam"]


class ChatCompletionToolMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPartTextParam]] = None
    # old  content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]
    """The contents of the tool message."""

    role: Literal["tool"] = None
    # old  role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: str = None
    # old  tool_call_id: Required[str]
    """Tool call that this message is responding to."""

