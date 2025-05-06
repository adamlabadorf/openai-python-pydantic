# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ToolChoiceTypesParam"]


class ToolChoiceTypesParam(BaseModel):
    type: "Literal['file_search', 'web_search_preview', 'computer_use_preview', 'web_search_preview_2025_03_11']"= None
    
    """The type of hosted tool the model should to use.

    Learn more about
    [built-in tools](https://platform.openai.com/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """
ToolChoiceTypesParam.model_rebuild()

