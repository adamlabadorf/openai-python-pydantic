import pytest
from pydantic import ValidationError

from openai_pydantic.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai_pydantic.types.chat.chat_completion_user_message_param import ChatCompletionUserMessageParam
from openai_pydantic.types.chat.chat_completion_system_message_param import ChatCompletionSystemMessageParam
from openai_pydantic.types.chat.chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam
from openai_pydantic.types.chat.chat_completion_tool_message_param import ChatCompletionToolMessageParam
from openai_pydantic.types.chat.chat_completion_function_message_param import ChatCompletionFunctionMessageParam
from openai_pydantic.types.chat.chat_completion_developer_message_param import ChatCompletionDeveloperMessageParam


def test_user_message_param():
    obj = ChatCompletionUserMessageParam(content="Hello", role="user", name="user1")
    assert obj.role == "user"
    assert obj.content == "Hello"
    assert obj.name == "user1"


def test_system_message_param():
    obj = ChatCompletionSystemMessageParam(content="System message", role="system", name="sys")
    assert obj.role == "system"
    assert obj.content == "System message"
    assert obj.name == "sys"


def test_assistant_message_param():
    obj = ChatCompletionAssistantMessageParam(role="assistant", content="Hi there!")
    assert obj.role == "assistant"
    assert obj.content == "Hi there!"


def test_tool_message_param():
    obj = ChatCompletionToolMessageParam(content="Tool response", role="tool", tool_call_id="call123")
    assert obj.role == "tool"
    assert obj.content == "Tool response"
    assert obj.tool_call_id == "call123"


def test_function_message_param():
    obj = ChatCompletionFunctionMessageParam(content="Function result", name="func", role="function")
    assert obj.role == "function"
    assert obj.content == "Function result"
    assert obj.name == "func"


def test_developer_message_param():
    obj = ChatCompletionDeveloperMessageParam(content="Dev message", role="developer", name="dev")
    assert obj.role == "developer"
    assert obj.content == "Dev message"
    assert obj.name == "dev"


def test_union_accepts_all_types():
    # The union is not a runtime type, but we can check isinstance for each
    for cls, kwargs in [
        (ChatCompletionUserMessageParam, dict(content="c", role="user")),
        (ChatCompletionSystemMessageParam, dict(content="c", role="system")),
        (ChatCompletionAssistantMessageParam, dict(content="c", role="assistant")),
        (ChatCompletionToolMessageParam, dict(content="c", role="tool", tool_call_id="id")),
        (ChatCompletionFunctionMessageParam, dict(content="c", role="function", name="n")),
        (ChatCompletionDeveloperMessageParam, dict(content="c", role="developer")),
    ]:
        obj = cls(**kwargs)
        assert isinstance(obj, ChatCompletionMessageParam.__args__)


def test_invalid_role_raises():
    with pytest.raises(ValidationError):
        ChatCompletionUserMessageParam(content="c", role="not_a_user")
    with pytest.raises(ValidationError):
        ChatCompletionToolMessageParam(content="c", role="not_a_tool", tool_call_id="id")


def test_missing_required_fields():
    with pytest.raises(ValidationError):
        ChatCompletionUserMessageParam(role="user")  # missing content
    with pytest.raises(ValidationError):
        ChatCompletionToolMessageParam(content="c", role="tool")  # missing tool_call_id
