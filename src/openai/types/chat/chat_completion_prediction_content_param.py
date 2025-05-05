# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionPredictionContentParam"]


class ChatCompletionPredictionContentParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPartTextParam]] = None
    # old  content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]
    """
    The content that should be matched when generating a model response. If
    generated tokens would match this content, the entire model response can be
    returned much more quickly.
    """

    type: Literal["content"] = None
    # old  type: Required[Literal["content"]]
    """The type of the predicted content you want to provide.

    This type is currently always `content`.
    """

