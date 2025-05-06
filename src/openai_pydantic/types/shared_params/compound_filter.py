# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

from .comparison_filter import ComparisonFilter

__all__ = ["CompoundFilter", "Filter"]

Filter = Union[ComparisonFilter, object]


class CompoundFilter(BaseModel):
    filters: "List[Filter]"= None
    
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: "Literal['and', 'or']"= None
    
    """Type of operation: `and` or `or`."""
CompoundFilter.model_rebuild()

