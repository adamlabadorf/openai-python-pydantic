# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,List
from typing_extensions import Literal

from .shared_params.metadata import Metadata
from .file_chunking_strategy_param import FileChunkingStrategyParam

__all__ = ["VectorStoreCreateParams", "ExpiresAfter"]


class VectorStoreCreateParams(BaseModel):
    chunking_strategy: "Optional[FileChunkingStrategyParam]"= None
    
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy. Only applicable if `file_ids` is
    non-empty.
    """

    expires_after: "Optional[ExpiresAfter]"= None
    
    """The expiration policy for a vector store."""

    file_ids: "Optional[List[str]]"= None
    
    """
    A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that
    the vector store should use. Useful for tools like `file_search` that can access
    files.
    """

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: "Optional[str]"= None
    
    """The name of the vector store."""


class ExpiresAfter(BaseModel):
    anchor: "Literal['last_active_at']"
    
    """Anchor timestamp after which the expiration policy applies.

    Supported anchors: `last_active_at`.
    """

    days: "int"
    
    """The number of days after the anchor time that the vector store will expire."""
VectorStoreCreateParams.model_rebuild()
ExpiresAfter.model_rebuild()

