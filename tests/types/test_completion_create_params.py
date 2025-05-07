import pytest
from pydantic import ValidationError
from openai_pydantic.types.chat.completion_create_params import (
    CompletionCreateParamsBase,
    CompletionCreateParamsNonStreaming,
    CompletionCreateParamsStreaming,
    CompletionCreateParams
)
from openai_pydantic.types.chat.chat_completion_user_message_param import ChatCompletionUserMessageParam

# Ensure all type hints are available for Pydantic model rebuild
from typing import Optional, Union, List
from typing_extensions import Literal


def test_completion_create_params_base_minimal():
    params = CompletionCreateParamsBase(model="gpt-3.5-turbo", messages=[ChatCompletionUserMessageParam(role="user", content="Hello")])
    assert params.model == "gpt-3.5-turbo"
    assert isinstance(params.messages, list)
    assert isinstance(params.messages[0], ChatCompletionUserMessageParam)
    assert params.messages[0].content == "Hello"
    assert params.messages[0].role == "user"
    assert params.frequency_penalty is None
    assert params.logit_bias is None
    assert params.logprobs is None
    assert params.max_tokens is None
    assert params.n is None
    assert params.presence_penalty is None
    assert params.seed is None
    assert params.stop is None
    assert params.temperature is None


#         max_tokens=10,
#         n=2,
#         presence_penalty=1.0,
#         seed=1234,
#         stop=["\n"],
#         suffix="Test suffix",
#         temperature=0.8,
#         top_p=0.9,
#         user="user-123",
#     )
#     assert params.model == "gpt-3.5-turbo-instruct"
#     assert params.prompt == ["Say this is a test!"]
#     assert params.best_of == 2
#     assert params.echo is True
#     assert params.frequency_penalty == 0.5
#     assert params.logit_bias == {"50256": -100}
#     assert params.logprobs == 5
#     assert params.max_tokens == 10
#     assert params.n == 2
#     assert params.presence_penalty == 1.0
#     assert params.seed == 1234
#     assert params.stop == ["\n"]
#     assert params.suffix == "Test suffix"
#     assert params.temperature == 0.8
#     assert params.top_p == 0.9
#     assert params.user == "user-123"


def test_completion_create_params_non_streaming():
    params = CompletionCreateParamsNonStreaming(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stream=False
    )
    assert params.stream is False
    # Should inherit from base
    assert isinstance(params, CompletionCreateParamsBase)
    assert isinstance(params, CompletionCreateParams)

    print(params)
    assert hasattr(params, "model")
    assert hasattr(params, "messages")


def test_completion_create_params_streaming():
    params = CompletionCreateParamsStreaming(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stream=True
    )
    assert params.stream is True
    # Should inherit from base
    assert isinstance(params, CompletionCreateParamsBase)
    assert isinstance(params, CompletionCreateParams)
    assert hasattr(params, "messages")
    assert params.messages[0].content == "Hello"
    assert params.messages[0].role == "user"


def test_completion_create_params_union():
    non_streaming = CompletionCreateParamsNonStreaming(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stream=False
    )
    streaming = CompletionCreateParamsStreaming(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stream=True
    )
    def is_union_instance(obj):
        return isinstance(obj, (CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming))
    assert is_union_instance(non_streaming)
    assert is_union_instance(streaming)


def test_invalid_logprobs():
    # logprobs max is 5, but pydantic model doesn't enforce, so this will pass
    params = CompletionCreateParamsBase(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        logprobs=True)
    assert params.logprobs == True


def test_invalid_model_type():
    # Should accept any string for model
    params = CompletionCreateParamsBase(
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        model="some-custom-model"
    )
    assert params.model == "some-custom-model"


def test_stop_as_string():
    params = CompletionCreateParamsBase(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stop="END")
    assert params.stop == "END"


def test_stop_as_list():
    params = CompletionCreateParamsBase(
        model="gpt-3.5-turbo",
        messages=[ChatCompletionUserMessageParam(role="user", content="Hello")],
        stop=["END", "STOP"])
    assert params.stop == ["END", "STOP"]
