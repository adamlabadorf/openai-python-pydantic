# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam

__all__ = ["ChatCompletionSystemMessageParam"]


class ChatCompletionSystemMessageParam(BaseModel):
    content: "Union[str, List[ChatCompletionContentPartTextParam]]"
    
    """The contents of the system message."""

    role: "Literal['system']"
    
    """The role of the messages author, in this case `system`."""

    name: "Optional[str]"= None
    
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """
ChatCompletionSystemMessageParam.model_rebuild()

