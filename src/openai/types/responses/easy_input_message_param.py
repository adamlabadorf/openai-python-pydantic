# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal
from pydantic import BaseModel
from .response_input_message_content_list_param import ResponseInputMessageContentListParam

__all__ = ["EasyInputMessageParam"]


class EasyInputMessageParam(BaseModel):
    content: Union[str, ResponseInputMessageContentListParam] = None
    # old  content: Required[Union[str, ResponseInputMessageContentListParam]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Literal["user", "assistant", "system", "developer"] = None
    # old  role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    # old  type: Literal["message"]
    """The type of the message input. Always `message`."""

