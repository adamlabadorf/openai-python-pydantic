# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ToolChoiceTypesParam"]


class ToolChoiceTypesParam(BaseModel):
    type:  Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11" ] = None
    # old  type: Required[ Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11"] ]
    """The type of hosted tool the model should to use.

    Learn more about
    [built-in tools](https://platform.openai.com/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """

