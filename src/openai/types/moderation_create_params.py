# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from pydantic import BaseModel
from .moderation_model import ModerationModel
from .moderation_multi_modal_input_param import ModerationMultiModalInputParam

__all__ = ["ModerationCreateParams"]


class ModerationCreateParams(BaseModel):
    input: Union[str, List[str], List[ModerationMultiModalInputParam]] = None
    # old  input: Required[Union[str, List[str], Iterable[ModerationMultiModalInputParam]]]
    """Input (or inputs) to classify.

    Can be a single string, an array of strings, or an array of multi-modal input
    objects similar to other models.
    """

    model: Optional[Union[str, ModerationModel]] = None
    # old  model: Union[str, ModerationModel]
    """The content moderation model you would like to use.

    Learn more in
    [the moderation guide](https://platform.openai.com/docs/guides/moderation), and
    learn about available models
    [here](https://platform.openai.com/docs/models#moderation).
    """

