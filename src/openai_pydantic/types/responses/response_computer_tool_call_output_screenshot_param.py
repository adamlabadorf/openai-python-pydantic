# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseComputerToolCallOutputScreenshotParam"]


class ResponseComputerToolCallOutputScreenshotParam(BaseModel):
    type: "Literal['computer_screenshot']"= None
    
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: "Optional[str]"= None
    
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: "Optional[str]"= None
    
    """The URL of the screenshot image."""
ResponseComputerToolCallOutputScreenshotParam.model_rebuild()

