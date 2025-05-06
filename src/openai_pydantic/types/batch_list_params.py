# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["BatchListParams"]


class BatchListParams(BaseModel):
    after: "Optional[str]"= None
    
    """A cursor for use in pagination.

    `after` is an object ID that defines your place in the list. For instance, if
    you make a list request and receive 100 objects, ending with obj_foo, your
    subsequent call can include after=obj_foo in order to fetch the next page of the
    list.
    """

    limit: "Optional[int]"= None
    
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """
BatchListParams.model_rebuild()

