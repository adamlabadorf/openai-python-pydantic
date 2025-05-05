# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import BaseModel
from .file_purpose import FilePurpose

__all__ = ["UploadCreateParams"]


class UploadCreateParams(BaseModel):
    bytes: int = None
    # old  bytes: Required[int]
    """The number of bytes in the file you are uploading."""

    filename: str = None
    # old  filename: Required[str]
    """The name of the file to upload."""

    mime_type: str = None
    # old  mime_type: Required[str]
    """The MIME type of the file.

    This must fall within the supported MIME types for your file purpose. See the
    supported MIME types for assistants and vision.
    """

    purpose: FilePurpose = None
    # old  purpose: Required[FilePurpose]
    """The intended purpose of the uploaded file.

    See the
    [documentation on File purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).
    """

