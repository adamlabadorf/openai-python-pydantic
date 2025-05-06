# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["EvalStringCheckGraderParam"]


class EvalStringCheckGraderParam(BaseModel):
    input: "str"= None
    
    """The input text. This may include template strings."""

    name: "str"= None
    
    """The name of the grader."""

    operation: "Literal['eq', 'ne', 'like', 'ilike']"= None
    
    """The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`."""

    reference: "str"= None
    
    """The reference text. This may include template strings."""

    type: "Literal['string_check']"= None
    
    """The object type, which is always `string_check`."""
EvalStringCheckGraderParam.model_rebuild()

