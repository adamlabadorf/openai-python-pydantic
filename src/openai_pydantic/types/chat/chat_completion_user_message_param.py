# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

from .chat_completion_content_part_param import ChatCompletionContentPartParam

__all__ = ["ChatCompletionUserMessageParam"]


class ChatCompletionUserMessageParam(BaseModel):
    content: "Union[str, List[ChatCompletionContentPartParam]]"= None
    
    """The contents of the user message."""

    role: "Literal['user']"= None
    
    """The role of the messages author, in this case `user`."""

    name: "Optional[str]"= None
    
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """
ChatCompletionUserMessageParam.model_rebuild()

