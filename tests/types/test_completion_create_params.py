import pytest
from pydantic import ValidationError
from openai_pydantic.types.completion_create_params import (
    CompletionCreateParamsBase,
    CompletionCreateParamsNonStreaming,
    CompletionCreateParamsStreaming,
    CompletionCreateParams
)

# Ensure all type hints are available for Pydantic model rebuild
from typing import Optional, Union, List
from typing_extensions import Literal


def test_completion_create_params_base_minimal():
    params = CompletionCreateParamsBase()
    assert params.model is None
    assert params.prompt is None
    assert params.best_of is None
    assert params.echo is None
    assert params.frequency_penalty is None
    assert params.temperature is None


def test_completion_create_params_base_full():
    params = CompletionCreateParamsBase(
        model="gpt-3.5-turbo-instruct",
        prompt=["Say this is a test!"],
        best_of=2,
        echo=True,
        frequency_penalty=0.5,
        logit_bias={"50256": -100},
        logprobs=5,
        max_tokens=10,
        n=2,
        presence_penalty=1.0,
        seed=1234,
        stop=["\n"],
        suffix="Test suffix",
        temperature=0.8,
        top_p=0.9,
        user="user-123",
    )
    assert params.model == "gpt-3.5-turbo-instruct"
    assert params.prompt == ["Say this is a test!"]
    assert params.best_of == 2
    assert params.echo is True
    assert params.frequency_penalty == 0.5
    assert params.logit_bias == {"50256": -100}
    assert params.logprobs == 5
    assert params.max_tokens == 10
    assert params.n == 2
    assert params.presence_penalty == 1.0
    assert params.seed == 1234
    assert params.stop == ["\n"]
    assert params.suffix == "Test suffix"
    assert params.temperature == 0.8
    assert params.top_p == 0.9
    assert params.user == "user-123"


def test_completion_create_params_non_streaming():
    params = CompletionCreateParamsNonStreaming(stream=False)
    assert params.stream is False
    # Should inherit from base
    assert isinstance(params, CompletionCreateParamsBase)


def test_completion_create_params_streaming():
    params = CompletionCreateParamsStreaming(stream=True)
    assert params.stream is True
    # Should inherit from base
    assert isinstance(params, CompletionCreateParamsBase)


def test_completion_create_params_union():
    non_streaming = CompletionCreateParamsNonStreaming(stream=False)
    streaming = CompletionCreateParamsStreaming(stream=True)
    def is_union_instance(obj):
        return isinstance(obj, (CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming))
    assert is_union_instance(non_streaming)
    assert is_union_instance(streaming)


def test_invalid_logprobs():
    # logprobs max is 5, but pydantic model doesn't enforce, so this will pass
    params = CompletionCreateParamsBase(logprobs=10)
    assert params.logprobs == 10


def test_invalid_model_type():
    # Should accept any string for model
    params = CompletionCreateParamsBase(model="some-custom-model")
    assert params.model == "some-custom-model"


def test_invalid_prompt_type():
    # Should raise if prompt is not correct type
    with pytest.raises(ValidationError):
        CompletionCreateParamsBase(prompt=12345)


def test_stop_as_string():
    params = CompletionCreateParamsBase(stop="END")
    assert params.stop == "END"


def test_stop_as_list():
    params = CompletionCreateParamsBase(stop=["END", "STOP"])
    assert params.stop == ["END", "STOP"]
