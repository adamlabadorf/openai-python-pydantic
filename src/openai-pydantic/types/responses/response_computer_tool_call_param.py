# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = [
    "ResponseComputerToolCallParam",
    "Action",
    "ActionClick",
    "ActionDoubleClick",
    "ActionDrag",
    "ActionDragPath",
    "ActionKeypress",
    "ActionMove",
    "ActionScreenshot",
    "ActionScroll",
    "ActionType",
    "ActionWait",
    "PendingSafetyCheck",
]


class ActionClick(BaseModel):
    button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Optional[Literal["left", "right", "wheel", "back", "forward"]] = None
    # old  button: Literal["left", "right", "wheel", "back", "forward"] = None
    # old  button: Required[Literal["left", "right", "wheel", "back", "forward"]]
    """Indicates which mouse button was pressed during the click.

    One of `left`, `right`, `wheel`, `back`, or `forward`.
    """

    type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Optional[Literal["click"]] = None
    # old  type: Literal["click"] = None
    # old  type: Required[Literal["click"]]
    """Specifies the event type.

    For a click action, this property is always set to `click`.
    """

    x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: int = None
    # old  x: Required[int]
    """The x-coordinate where the click occurred."""

    y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: int = None
    # old  y: Required[int]
    """The y-coordinate where the click occurred."""


class ActionDoubleClick(BaseModel):
    type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Optional[Literal["double_click"]] = None
    # old  type: Literal["double_click"] = None
    # old  type: Required[Literal["double_click"]]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: int = None
    # old  x: Required[int]
    """The x-coordinate where the double click occurred."""

    y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: int = None
    # old  y: Required[int]
    """The y-coordinate where the double click occurred."""


class ActionDragPath(BaseModel):
    x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: int = None
    # old  x: Required[int]
    """The x-coordinate."""

    y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: int = None
    # old  y: Required[int]
    """The y-coordinate."""


class ActionDrag(BaseModel):
    path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: Optional[List[ActionDragPath]] = None
    # old  path: List[ActionDragPath] = None
    # old  path: Required[Iterable[ActionDragPath]]
    """An array of coordinates representing the path of the drag action.

    Coordinates will appear as an array of objects, eg

    ```
    [
      { x: 100, y: 200 },
      { x: 200, y: 300 }
    ]
    ```
    """

    type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Optional[Literal["drag"]] = None
    # old  type: Literal["drag"] = None
    # old  type: Required[Literal["drag"]]
    """Specifies the event type.

    For a drag action, this property is always set to `drag`.
    """


class ActionKeypress(BaseModel):
    keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: Optional[List[str]] = None
    # old  keys: List[str] = None
    # old  keys: Required[List[str]]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Optional[Literal["keypress"]] = None
    # old  type: Literal["keypress"] = None
    # old  type: Required[Literal["keypress"]]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class ActionMove(BaseModel):
    type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Optional[Literal["move"]] = None
    # old  type: Literal["move"] = None
    # old  type: Required[Literal["move"]]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: int = None
    # old  x: Required[int]
    """The x-coordinate to move to."""

    y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: int = None
    # old  y: Required[int]
    """The y-coordinate to move to."""


class ActionScreenshot(BaseModel):
    type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Optional[Literal["screenshot"]] = None
    # old  type: Literal["screenshot"] = None
    # old  type: Required[Literal["screenshot"]]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class ActionScroll(BaseModel):
    scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: Optional[int] = None
    # old  scroll_x: int = None
    # old  scroll_x: Required[int]
    """The horizontal scroll distance."""

    scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: Optional[int] = None
    # old  scroll_y: int = None
    # old  scroll_y: Required[int]
    """The vertical scroll distance."""

    type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Optional[Literal["scroll"]] = None
    # old  type: Literal["scroll"] = None
    # old  type: Required[Literal["scroll"]]
    """Specifies the event type.

    For a scroll action, this property is always set to `scroll`.
    """

    x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: Optional[int] = None
    # old  x: int = None
    # old  x: Required[int]
    """The x-coordinate where the scroll occurred."""

    y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: Optional[int] = None
    # old  y: int = None
    # old  y: Required[int]
    """The y-coordinate where the scroll occurred."""


class ActionType(BaseModel):
    text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: str = None
    # old  text: Required[str]
    """The text to type."""

    type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Optional[Literal["type"]] = None
    # old  type: Literal["type"] = None
    # old  type: Required[Literal["type"]]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class ActionWait(BaseModel):
    type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Optional[Literal["wait"]] = None
    # old  type: Literal["wait"] = None
    # old  type: Required[Literal["wait"]]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


Action = Union[ # old Action: TypeAlias = Union[
    ActionClick,
    ActionDoubleClick,
    ActionDrag,
    ActionKeypress,
    ActionMove,
    ActionScreenshot,
    ActionScroll,
    ActionType,
    ActionWait,
]


class PendingSafetyCheck(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
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
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: Optional[str] = None
    # old  code: str = None
    # old  code: Required[str]
    """The type of the pending safety check."""

    message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: Optional[str] = None
    # old  message: str = None
    # old  message: Required[str]
    """Details about the pending safety check."""


class ResponseComputerToolCallParam(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The unique ID of the computer call."""

    action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Optional[Action] = None
    # old  action: Action = None
    # old  action: Required[Action]
    """A click action."""

    call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: Optional[str] = None
    # old  call_id: str = None
    # old  call_id: Required[str]
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: Optional[List[PendingSafetyCheck]] = None
    # old  pending_safety_checks: List[PendingSafetyCheck] = None
    # old  pending_safety_checks: Required[Iterable[PendingSafetyCheck]]
    """The pending safety checks for the computer call."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    # old  status: Literal["in_progress", "completed", "incomplete"] = None
    # old  status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Optional[Literal["computer_call"]] = None
    # old  type: Literal["computer_call"] = None
    # old  type: Required[Literal["computer_call"]]
    """The type of the computer call. Always `computer_call`."""












