# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseInputFileParam"]


class ResponseInputFileParam(BaseModel):
    type: Literal["input_file"] = None
    # old  type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    # old  file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    # old  file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    filename: Optional[str] = None
    # old  filename: str
    """The name of the file to be sent to the model."""

