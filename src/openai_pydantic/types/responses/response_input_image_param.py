# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["ResponseInputImageParam"]


class ResponseInputImageParam(BaseModel):
    detail: "Literal['low', 'high', 'auto']"= None
    
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: "Literal['input_image']"= None
    
    """The type of the input item. Always `input_image`."""

    file_id: "Optional[str]"= None
    
    """The ID of the file to be sent to the model."""

    image_url: "Optional[str]"= None
    
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """
ResponseInputImageParam.model_rebuild()

