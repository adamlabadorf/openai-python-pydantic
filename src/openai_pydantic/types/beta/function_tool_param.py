# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

from ..shared_params.function_definition import FunctionDefinition

__all__ = ["FunctionToolParam"]


class FunctionToolParam(BaseModel):
    function: "FunctionDefinition"
    

    type: "Literal['function']"
    
    """The type of tool being defined: `function`"""
FunctionToolParam.model_rebuild()

