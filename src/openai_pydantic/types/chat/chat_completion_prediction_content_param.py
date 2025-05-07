# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionPredictionContentParam"]


class ChatCompletionPredictionContentParam(BaseModel):
    content: "Union[str, List[ChatCompletionContentPartTextParam]]"
    
    """
    The content that should be matched when generating a model response. If
    generated tokens would match this content, the entire model response can be
    returned much more quickly.
    """

    type: "Literal['content']"
    
    """The type of the predicted content you want to provide.

    This type is currently always `content`.
    """
ChatCompletionPredictionContentParam.model_rebuild()

