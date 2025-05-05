# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = [
    "RunSubmitToolOutputsParamsBase",
    "ToolOutput",
    "RunSubmitToolOutputsParamsNonStreaming",
    "RunSubmitToolOutputsParamsStreaming",
]


class RunSubmitToolOutputsParamsBase(BaseModel):
    thread_id: Optional[str] = None
    # old  thread_id: str = None
    # old  thread_id: Required[str]

    tool_outputs: Optional[List[ToolOutput]] = None
    # old  tool_outputs: List[ToolOutput] = None
    # old  tool_outputs: Required[Iterable[ToolOutput]]
    """A list of tools for which the outputs are being submitted."""


class ToolOutput(BaseModel):
    output: Optional[str] = None
    # old  output: Optional[str] = None
    # old  output: str
    """The output of the tool call to be submitted to continue the run."""

    tool_call_id: Optional[str] = None
    # old  tool_call_id: Optional[str] = None
    # old  tool_call_id: str
    """
    The ID of the tool call in the `required_action` object within the run object
    the output is being submitted for.
    """


class RunSubmitToolOutputsParamsNonStreaming(RunSubmitToolOutputsParamsBase):
    stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


class RunSubmitToolOutputsParamsStreaming(RunSubmitToolOutputsParamsBase):
    stream: Optional[Literal[True]] = None
    # old  stream: Literal[True] = None
    # old  stream: Required[Literal[True]]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


RunSubmitToolOutputsParams = Union[RunSubmitToolOutputsParamsNonStreaming, RunSubmitToolOutputsParamsStreaming]


