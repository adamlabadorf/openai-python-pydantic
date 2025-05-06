# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import List,Optional
from typing_extensions import Literal

from .response_includable import ResponseIncludable

__all__ = ["InputItemListParams"]


class InputItemListParams(BaseModel):
    after: "Optional[str]"= None
    
    """An item ID to list items after, used in pagination."""

    before: "Optional[str]"= None
    
    """An item ID to list items before, used in pagination."""

    include: "Optional[List[ResponseIncludable]]"= None
    
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """

    limit: "Optional[int]"= None
    
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """The order to return the input items in. Default is `asc`.

    - `asc`: Return the input items in ascending order.
    - `desc`: Return the input items in descending order.
    """
InputItemListParams.model_rebuild()

