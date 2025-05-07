# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["CodeInterpreterToolParam"]


class CodeInterpreterToolParam(BaseModel):
    type: "Literal['code_interpreter']"
    
    """The type of tool being defined: `code_interpreter`"""
CodeInterpreterToolParam.model_rebuild()

