# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


from .._types import FileTypes
from .file_purpose import FilePurpose

__all__ = ["FileCreateParams"]


class FileCreateParams(BaseModel):
    file: "FileTypes"= None
    
    """The File object (not file name) to be uploaded."""

    purpose: "FilePurpose"= None
    
    """The intended purpose of the uploaded file.

    One of: - `assistants`: Used in the Assistants API - `batch`: Used in the Batch
    API - `fine-tune`: Used for fine-tuning - `vision`: Images used for vision
    fine-tuning - `user_data`: Flexible file type for any purpose - `evals`: Used
    for eval data sets
    """
FileCreateParams.model_rebuild()

