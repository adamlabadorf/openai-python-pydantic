# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

from .response_input_message_content_list_param import ResponseInputMessageContentListParam

__all__ = ["EasyInputMessageParam"]


class EasyInputMessageParam(BaseModel):
    content: "Union[str, ResponseInputMessageContentListParam]"= None
    
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: "Literal['user', 'assistant', 'system', 'developer']"= None
    
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: "Optional[Literal['message']]"= None
    
    """The type of the message input. Always `message`."""
EasyInputMessageParam.model_rebuild()

