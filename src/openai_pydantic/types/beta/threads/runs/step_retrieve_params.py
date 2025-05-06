# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import List,Optional

from .run_step_include import RunStepInclude

__all__ = ["StepRetrieveParams"]


class StepRetrieveParams(BaseModel):
    thread_id: "str"= None
    

    run_id: "str"= None
    

    include: "Optional[List[RunStepInclude]]"= None
    
    """A list of additional fields to include in the response.

    Currently the only supported value is
    `step_details.tool_calls[*].file_search.results[*].content` to fetch the file
    search result content.

    See the
    [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """
StepRetrieveParams.model_rebuild()

