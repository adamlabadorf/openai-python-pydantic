# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional
from typing_extensions import Literal

__all__ = [
    "RunSubmitToolOutputsParamsBase",
    "ToolOutput",
    "RunSubmitToolOutputsParamsNonStreaming",
    "RunSubmitToolOutputsParamsStreaming",
]


class RunSubmitToolOutputsParamsBase(BaseModel):
    thread_id: "str"
    

    tool_outputs: "List[ToolOutput]"
    
    """A list of tools for which the outputs are being submitted."""


class ToolOutput(BaseModel):
    output: "Optional[str]"= None
    
    """The output of the tool call to be submitted to continue the run."""

    tool_call_id: "Optional[str]"= None
    
    """
    The ID of the tool call in the `required_action` object within the run object
    the output is being submitted for.
    """


class RunSubmitToolOutputsParamsNonStreaming(RunSubmitToolOutputsParamsBase):
    stream: "Optional[Literal[False]]"= None
    
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


class RunSubmitToolOutputsParamsStreaming(RunSubmitToolOutputsParamsBase):
    stream: "Literal[True]"
    
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


RunSubmitToolOutputsParams = Union[RunSubmitToolOutputsParamsNonStreaming, RunSubmitToolOutputsParamsStreaming]
RunSubmitToolOutputsParamsBase.model_rebuild()
ToolOutput.model_rebuild()
RunSubmitToolOutputsParamsNonStreaming.model_rebuild()
RunSubmitToolOutputsParamsStreaming.model_rebuild()

