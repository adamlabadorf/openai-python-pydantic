# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ToolChoiceFunctionParam"]


class ToolChoiceFunctionParam(BaseModel):
    name: str = None
    # old  name: Required[str]
    """The name of the function to call."""

    type: Literal["function"] = None
    # old  type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""

