# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,List,Optional
from typing_extensions import Literal

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
    button: "Literal['left', 'right', 'wheel', 'back', 'forward']"= None
    
    """Indicates which mouse button was pressed during the click.

    One of `left`, `right`, `wheel`, `back`, or `forward`.
    """

    type: "Literal['click']"= None
    
    """Specifies the event type.

    For a click action, this property is always set to `click`.
    """

    x: "int"= None
    
    """The x-coordinate where the click occurred."""

    y: "int"= None
    
    """The y-coordinate where the click occurred."""


class ActionDoubleClick(BaseModel):
    type: "Literal['double_click']"= None
    
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: "int"= None
    
    """The x-coordinate where the double click occurred."""

    y: "int"= None
    
    """The y-coordinate where the double click occurred."""


class ActionDragPath(BaseModel):
    x: "int"= None
    
    """The x-coordinate."""

    y: "int"= None
    
    """The y-coordinate."""


class ActionDrag(BaseModel):
    path: "List[ActionDragPath]"= None
    
    """An array of coordinates representing the path of the drag action.

    Coordinates will appear as an array of objects, eg

    ```
    [
      { x: 100, y: 200 },
      { x: 200, y: 300 }
    ]
    ```
    """

    type: "Literal['drag']"= None
    
    """Specifies the event type.

    For a drag action, this property is always set to `drag`.
    """


class ActionKeypress(BaseModel):
    keys: "List[str]"= None
    
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: "Literal['keypress']"= None
    
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class ActionMove(BaseModel):
    type: "Literal['move']"= None
    
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: "int"= None
    
    """The x-coordinate to move to."""

    y: "int"= None
    
    """The y-coordinate to move to."""


class ActionScreenshot(BaseModel):
    type: "Literal['screenshot']"= None
    
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class ActionScroll(BaseModel):
    scroll_x: "int"= None
    
    """The horizontal scroll distance."""

    scroll_y: "int"= None
    
    """The vertical scroll distance."""

    type: "Literal['scroll']"= None
    
    """Specifies the event type.

    For a scroll action, this property is always set to `scroll`.
    """

    x: "int"= None
    
    """The x-coordinate where the scroll occurred."""

    y: "int"= None
    
    """The y-coordinate where the scroll occurred."""


class ActionType(BaseModel):
    text: "str"= None
    
    """The text to type."""

    type: "Literal['type']"= None
    
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class ActionWait(BaseModel):
    type: "Literal['wait']"= None
    
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


Action = Union[
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
    id: "str"= None
    
    """The ID of the pending safety check."""

    code: "str"= None
    
    """The type of the pending safety check."""

    message: "str"= None
    
    """Details about the pending safety check."""


class ResponseComputerToolCallParam(BaseModel):
    id: "str"= None
    
    """The unique ID of the computer call."""

    action: "Action"= None
    
    """A click action."""

    call_id: "str"= None
    
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: "List[PendingSafetyCheck]"= None
    
    """The pending safety checks for the computer call."""

    status: "Literal['in_progress', 'completed', 'incomplete']"= None
    
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: "Literal['computer_call']"= None
    
    """The type of the computer call. Always `computer_call`."""
ActionClick.model_rebuild()
ActionDoubleClick.model_rebuild()
ActionDragPath.model_rebuild()
ActionDrag.model_rebuild()
ActionKeypress.model_rebuild()
ActionMove.model_rebuild()
ActionScreenshot.model_rebuild()
ActionScroll.model_rebuild()
ActionType.model_rebuild()
ActionWait.model_rebuild()
PendingSafetyCheck.model_rebuild()
ResponseComputerToolCallParam.model_rebuild()

