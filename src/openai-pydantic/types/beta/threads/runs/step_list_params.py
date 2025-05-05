# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal
from pydantic import BaseModel
from .run_step_include import RunStepInclude

__all__ = ["StepListParams"]


class StepListParams(BaseModel):
    thread_id: str = None
    # old  thread_id: Required[str]

    after: Optional[str] = None
    # old  after: str
    """A cursor for use in pagination.

    `after` is an object ID that defines your place in the list. For instance, if
    you make a list request and receive 100 objects, ending with obj_foo, your
    subsequent call can include after=obj_foo in order to fetch the next page of the
    list.
    """

    before: Optional[str] = None
    # old  before: str
    """A cursor for use in pagination.

    `before` is an object ID that defines your place in the list. For instance, if
    you make a list request and receive 100 objects, starting with obj_foo, your
    subsequent call can include before=obj_foo in order to fetch the previous page
    of the list.
    """

    include: Optional[List[RunStepInclude]] = None
    # old  include: List[RunStepInclude]
    """A list of additional fields to include in the response.

    Currently the only supported value is
    `step_details.tool_calls[*].file_search.results[*].content` to fetch the file
    search result content.

    See the
    [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """

    limit: Optional[int] = None
    # old  limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """Sort order by the `created_at` timestamp of the objects.

    `asc` for ascending order and `desc` for descending order.
    """

