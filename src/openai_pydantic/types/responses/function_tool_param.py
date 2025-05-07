# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Dict
from typing_extensions import Literal

__all__ = ["FunctionToolParam"]


class FunctionToolParam(BaseModel):
    name: "str"
    
    """The name of the function to call."""

    parameters: "Optional[Dict[str, object]]"
    
    """A JSON schema object describing the parameters of the function."""

    strict: "Optional[bool]"
    
    """Whether to enforce strict parameter validation. Default `true`."""

    type: "Literal['function']"
    
    """The type of the function tool. Always `function`."""

    description: "Optional[str]"= None
    
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """
FunctionToolParam.model_rebuild()

