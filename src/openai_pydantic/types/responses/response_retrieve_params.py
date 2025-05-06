# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,List

from .response_includable import ResponseIncludable

__all__ = ["ResponseRetrieveParams"]


class ResponseRetrieveParams(BaseModel):
    include: "Optional[List[ResponseIncludable]]"= None
    
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """
ResponseRetrieveParams.model_rebuild()

