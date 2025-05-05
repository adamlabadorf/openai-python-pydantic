# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal
from pydantic import BaseModel
from .response_includable import ResponseIncludable

__all__ = ["InputItemListParams"]


class InputItemListParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """An item ID to list items after, used in pagination."""

    before: Optional[str] = None
    # old  before: str
    """An item ID to list items before, used in pagination."""

    include: Optional[List[ResponseIncludable]] = None
    # old  include: List[ResponseIncludable]
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """

    limit: Optional[int] = None
    # old  limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """The order to return the input items in. Default is `asc`.

    - `asc`: Return the input items in ascending order.
    - `desc`: Return the input items in descending order.
    """

