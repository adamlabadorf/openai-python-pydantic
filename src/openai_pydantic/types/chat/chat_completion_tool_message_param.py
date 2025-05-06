# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionToolMessageParam"]


class ChatCompletionToolMessageParam(BaseModel):
    content: "Union[str, List[ChatCompletionContentPartTextParam]]"= None
    
    """The contents of the tool message."""

    role: "Literal['tool']"= None
    
    """The role of the messages author, in this case `tool`."""

    tool_call_id: "str"= None
    
    """Tool call that this message is responding to."""
ChatCompletionToolMessageParam.model_rebuild()

