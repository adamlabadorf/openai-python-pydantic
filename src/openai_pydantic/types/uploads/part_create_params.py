# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


from ..._types import FileTypes

__all__ = ["PartCreateParams"]


class PartCreateParams(BaseModel):
    data: "FileTypes"= None
    
    """The chunk of bytes for this Part."""
PartCreateParams.model_rebuild()

