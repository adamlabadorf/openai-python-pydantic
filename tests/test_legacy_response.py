import json
from typing import Any, Union, cast
from typing_extensions import Annotated

import httpx
import pytest
import pydantic

from openai_pydantic import OpenAI, BaseModel
from openai_pydantic._streaming import Stream
from openai_pydantic._base_client import FinalRequestOptions
from openai_pydantic._legacy_response import LegacyAPIResponse

from .utils import rich_print_str


class PydanticModel(pydantic.BaseModel): ...


def test_response_parse_mismatched_basemodel(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    with pytest.raises(
        TypeError,
        match="Pydantic models must subclass our base model type, e.g. `from openai_pydantic import BaseModel`",
    ):
        response.parse(to=PydanticModel)


@pytest.mark.parametrize(
    "content, expected",
    [
        ("false", False),
        ("true", True),
        ("False", False),
        ("True", True),
        ("TrUe", True),
        ("FalSe", False),
    ],
)
def test_response_parse_bool(client: OpenAI, content: str, expected: bool) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=content),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    result = response.parse(to=bool)
    assert result is expected


def test_response_parse_custom_stream(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=client,
        stream=True,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    stream = response.parse(to=Stream[int])
    assert stream._cast_to == int


class CustomModel(BaseModel):
    foo: str
    bar: int


def test_response_parse_custom_model(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(to=CustomModel)
    assert obj.foo == "hello!"
    assert obj.bar == 2


def test_response_basemodel_request_id(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(
            200,
            headers={"x-request-id": "my-req-id"},
            content=json.dumps({"foo": "hello!", "bar": 2}),
        ),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(to=CustomModel)
    assert obj._request_id == "my-req-id"
    assert obj.foo == "hello!"
    assert obj.bar == 2
    assert obj.to_dict() == {"foo": "hello!", "bar": 2}
    assert "_request_id" not in rich_print_str(obj)
    assert "__exclude_fields__" not in rich_print_str(obj)


def test_response_parse_annotated_type(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(
        to=cast("type[CustomModel]", Annotated[CustomModel, "random metadata"]),
    )
    assert obj.foo == "hello!"
    assert obj.bar == 2


class OtherModel(pydantic.BaseModel):
    a: str


@pytest.mark.parametrize("client", [False], indirect=True)  # loose validation
def test_response_parse_expect_model_union_non_json_content(client: OpenAI) -> None:
    response = LegacyAPIResponse(
        raw=httpx.Response(200, content=b"foo", headers={"Content-Type": "application/text"}),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(to=cast(Any, Union[CustomModel, OtherModel]))
    assert isinstance(obj, str)
    assert obj == "foo"
