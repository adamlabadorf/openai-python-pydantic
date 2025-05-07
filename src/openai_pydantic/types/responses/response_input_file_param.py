# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["ResponseInputFileParam"]


class ResponseInputFileParam(BaseModel):
    type: "Literal['input_file']"
    
    """The type of the input item. Always `input_file`."""

    file_data: "Optional[str]"= None
    
    """The content of the file to be sent to the model."""

    file_id: "Optional[str]"= None
    
    """The ID of the file to be sent to the model."""

    filename: "Optional[str]"= None
    
    """The name of the file to be sent to the model."""
ResponseInputFileParam.model_rebuild()

