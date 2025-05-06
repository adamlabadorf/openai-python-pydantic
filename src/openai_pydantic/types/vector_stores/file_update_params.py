# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Dict,Optional,Union

__all__ = ["FileUpdateParams"]


class FileUpdateParams(BaseModel):
    vector_store_id: "str"= None
    

    attributes: "Optional[Dict[str, Union[str, float, bool]]]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """
FileUpdateParams.model_rebuild()

