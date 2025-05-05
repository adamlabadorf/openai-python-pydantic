# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["CodeInterpreterToolParam"]


class CodeInterpreterToolParam(BaseModel):
    type: Literal["code_interpreter"] = None
    # old  type: Required[Literal["code_interpreter"]]
    """The type of tool being defined: `code_interpreter`"""

