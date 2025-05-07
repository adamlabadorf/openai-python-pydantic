# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


from .file_purpose import FilePurpose

__all__ = ["UploadCreateParams"]


class UploadCreateParams(BaseModel):
    bytes: "int"
    
    """The number of bytes in the file you are uploading."""

    filename: "str"
    
    """The name of the file to upload."""

    mime_type: "str"
    
    """The MIME type of the file.

    This must fall within the supported MIME types for your file purpose. See the
    supported MIME types for assistants and vision.
    """

    purpose: "FilePurpose"
    
    """The intended purpose of the uploaded file.

    See the
    [documentation on File purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).
    """
UploadCreateParams.model_rebuild()

