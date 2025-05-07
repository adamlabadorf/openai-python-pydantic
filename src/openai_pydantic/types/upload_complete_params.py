# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,List

__all__ = ["UploadCompleteParams"]


class UploadCompleteParams(BaseModel):
    part_ids: "List[str]"
    
    """The ordered list of Part IDs."""

    md5: "Optional[str]"= None
    
    """
    The optional md5 checksum for the file contents to verify if the bytes uploaded
    matches what you expect.
    """
UploadCompleteParams.model_rebuild()

