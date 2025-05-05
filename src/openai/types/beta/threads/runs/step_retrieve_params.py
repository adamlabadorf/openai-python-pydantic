# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from pydantic import BaseModel
from .run_step_include import RunStepInclude

__all__ = ["StepRetrieveParams"]


class StepRetrieveParams(BaseModel):
    thread_id: str = None
    # old  thread_id: Required[str]

    run_id: str = None
    # old  run_id: Required[str]

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

