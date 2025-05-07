# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union
from typing_extensions import Literal

__all__ = ["ComparisonFilter"]


class ComparisonFilter(BaseModel):
    key: "str"
    
    """The key to compare against the value."""

    type: "Literal['eq', 'ne', 'gt', 'gte', 'lt', 'lte']"
    
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: "Union[str, float, bool]"
    
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """
ComparisonFilter.model_rebuild()

