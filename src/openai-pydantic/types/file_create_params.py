# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import BaseModel
from .._types import FileTypes
from .file_purpose import FilePurpose

__all__ = ["FileCreateParams"]


class FileCreateParams(BaseModel):
    file: FileTypes = None
    # old  file: Required[FileTypes]
    """The File object (not file name) to be uploaded."""

    purpose: FilePurpose = None
    # old  purpose: Required[FilePurpose]
    """The intended purpose of the uploaded file.

    One of: - `assistants`: Used in the Assistants API - `batch`: Used in the Batch
    API - `fine-tune`: Used for fine-tuning - `vision`: Images used for vision
    fine-tuning - `user_data`: Flexible file type for any purpose - `evals`: Used
    for eval data sets
    """

