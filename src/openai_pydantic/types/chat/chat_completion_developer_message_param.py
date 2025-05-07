# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionDeveloperMessageParam"]


class ChatCompletionDeveloperMessageParam(BaseModel):
    content: "Union[str, List[ChatCompletionContentPartTextParam]]"
    
    """The contents of the developer message."""

    role: "Literal['developer']"
    
    """The role of the messages author, in this case `developer`."""

    name: "Optional[str]"= None
    
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """
ChatCompletionDeveloperMessageParam.model_rebuild()

