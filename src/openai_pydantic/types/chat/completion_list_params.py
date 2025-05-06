# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

from ..shared_params.metadata import Metadata

__all__ = ["CompletionListParams"]


class CompletionListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last chat completion from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of Chat Completions to retrieve."""

    metadata: "Optional[Metadata]"= None
    
    """A list of metadata keys to filter the Chat Completions by. Example:

    `metadata[key1]=value1&metadata[key2]=value2`
    """

    model: "Optional[str]"= None
    
    """The model used to generate the Chat Completions."""

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """Sort order for Chat Completions by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """
CompletionListParams.model_rebuild()

