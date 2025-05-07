# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseOutputRefusalParam"]


class ResponseOutputRefusalParam(BaseModel):
    refusal: "str"
    
    """The refusal explanationfrom the model."""

    type: "Literal['refusal']"
    
    """The type of the refusal. Always `refusal`."""
ResponseOutputRefusalParam.model_rebuild()

