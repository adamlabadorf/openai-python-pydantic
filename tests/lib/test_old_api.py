import pytest

import openai_pydantic
from openai_pydantic.lib._old_api import APIRemovedInV1


def test_basic_attribute_access_works() -> None:
    for attr in dir(openai_pydantic):
        getattr(openai_pydantic, attr)


def test_helpful_error_is_raised() -> None:
    with pytest.raises(APIRemovedInV1):
        openai_pydantic.Completion.create()  # type: ignore

    with pytest.raises(APIRemovedInV1):
        openai_pydantic.ChatCompletion.create()  # type: ignore
