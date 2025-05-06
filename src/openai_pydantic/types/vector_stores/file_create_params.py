# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Dict,Optional

from ..file_chunking_strategy_param import FileChunkingStrategyParam

__all__ = ["FileCreateParams"]


class FileCreateParams(BaseModel):
    file_id: "str"= None
    
    """
    A [File](https://platform.openai.com/docs/api-reference/files) ID that the
    vector store should use. Useful for tools like `file_search` that can access
    files.
    """

    attributes: "Optional[Dict[str, Union[str, float, bool]]]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    chunking_strategy: "Optional[FileChunkingStrategyParam]"= None
    
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy. Only applicable if `file_ids` is
    non-empty.
    """
FileCreateParams.model_rebuild()

