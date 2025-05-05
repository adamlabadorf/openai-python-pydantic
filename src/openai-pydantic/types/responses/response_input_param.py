# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from .easy_input_message_param import EasyInputMessageParam
from .response_output_message_param import ResponseOutputMessageParam
from .response_reasoning_item_param import ResponseReasoningItemParam
from .response_computer_tool_call_param import ResponseComputerToolCallParam
from .response_function_tool_call_param import ResponseFunctionToolCallParam
from .response_function_web_search_param import ResponseFunctionWebSearchParam
from .response_file_search_tool_call_param import ResponseFileSearchToolCallParam
from .response_input_message_content_list_param import ResponseInputMessageContentListParam
from .response_computer_tool_call_output_screenshot_param import ResponseComputerToolCallOutputScreenshotParam

__all__ = [
    "ResponseInputParam",
    "ResponseInputItemParam",
    "Message",
    "ComputerCallOutput",
    "ComputerCallOutputAcknowledgedSafetyCheck",
    "FunctionCallOutput",
    "ItemReference",
]


class Message(BaseModel):
    content: Optional[ResponseInputMessageContentListParam] = None
    # old  content: Optional[ResponseInputMessageContentListParam] = None
    # old  content: Optional[ResponseInputMessageContentListParam] = None
    # old  content: Optional[ResponseInputMessageContentListParam] = None
    # old  content: ResponseInputMessageContentListParam = None
    # old  content: Required[ResponseInputMessageContentListParam]
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Optional[Literal["user", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "system", "developer"]] = None
    # old  role: Literal["user", "system", "developer"] = None
    # old  role: Required[Literal["user", "system", "developer"]]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Literal["in_progress", "completed", "incomplete"]
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Literal["message"]
    """The type of the message input. Always set to `message`."""


class ComputerCallOutputAcknowledgedSafetyCheck(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The ID of the pending safety check."""

    code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str]
    """The type of the pending safety check."""

    message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str]
    """Details about the pending safety check."""


class ComputerCallOutput(BaseModel):
    call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: str = None
    # old  call_id: Required[str]
    """The ID of the computer tool call that produced the output."""

    output: Optional[ResponseComputerToolCallOutputScreenshotParam] = None
    # old  output: Optional[ResponseComputerToolCallOutputScreenshotParam] = None
    # old  output: Optional[ResponseComputerToolCallOutputScreenshotParam] = None
    # old  output: Optional[ResponseComputerToolCallOutputScreenshotParam] = None
    # old  output: ResponseComputerToolCallOutputScreenshotParam = None
    # old  output: Required[ResponseComputerToolCallOutputScreenshotParam]
    """A computer screenshot image used with the computer use tool."""

    type: Optional[Literal["computer_call_output"]] = None
    # old  type: Optional[Literal["computer_call_output"]] = None
    # old  type: Optional[Literal["computer_call_output"]] = None
    # old  type: Optional[Literal["computer_call_output"]] = None
    # old  type: Literal["computer_call_output"] = None
    # old  type: Required[Literal["computer_call_output"]]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str]
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    # old  acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    # old  acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    # old  acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    # old  acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    # old  acknowledged_safety_checks: Optional[Iterable[ComputerCallOutputAcknowledgedSafetyCheck]]
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class FunctionCallOutput(BaseModel):
    call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: str = None
    # old  call_id: Required[str]
    """The unique ID of the function tool call generated by the model."""

    output: Optional[str] = None
    # old  output: Optional[str] = None
    # old  output: Optional[str] = None
    # old  output: Optional[str] = None
    # old  output: str = None
    # old  output: Required[str]
    """A JSON string of the output of the function tool call."""

    type: Optional[Literal["function_call_output"]] = None
    # old  type: Optional[Literal["function_call_output"]] = None
    # old  type: Optional[Literal["function_call_output"]] = None
    # old  type: Optional[Literal["function_call_output"]] = None
    # old  type: Literal["function_call_output"] = None
    # old  type: Required[Literal["function_call_output"]]
    """The type of the function tool call output. Always `function_call_output`."""

    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str]
    """The unique ID of the function tool call output.

    Populated when this item is returned via API.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class ItemReference(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


ResponseInputItemParam = Union[ # old ResponseInputItemParam: TypeAlias = Union[
    EasyInputMessageParam,
    Message,
    ResponseOutputMessageParam,
    ResponseFileSearchToolCallParam,
    ResponseComputerToolCallParam,
    ComputerCallOutput,
    ResponseFunctionWebSearchParam,
    ResponseFunctionToolCallParam,
    FunctionCallOutput,
    ResponseReasoningItemParam,
    ItemReference,
]

ResponseInputParam = List[ResponseInputItemParam] # old ResponseInputParam: TypeAlias = List[ResponseInputItemParam]





