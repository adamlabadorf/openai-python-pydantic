# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os as _os

import httpx
import pytest
from httpx import URL

import openai_pydantic
from openai_pydantic import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    openai_pydantic._reset_client()
    openai_pydantic.api_key = None or "My API Key"
    openai_pydantic.organization = None
    openai_pydantic.project = None
    openai_pydantic.base_url = None
    openai_pydantic.timeout = DEFAULT_TIMEOUT
    openai_pydantic.max_retries = DEFAULT_MAX_RETRIES
    openai_pydantic.default_headers = None
    openai_pydantic.default_query = None
    openai_pydantic.http_client = None
    openai_pydantic.api_type = _os.environ.get("OPENAI_API_TYPE")  # type: ignore
    openai_pydantic.api_version = None
    openai_pydantic.azure_endpoint = None
    openai_pydantic.azure_ad_token = None
    openai_pydantic.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert openai_pydantic.base_url is None
    assert openai_pydantic.completions._client.base_url == URL("https://api.openai_pydantic.com/v1/")

    openai_pydantic.base_url = "http://foo.com"

    assert openai_pydantic.base_url == URL("http://foo.com")
    assert openai_pydantic.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert openai_pydantic.timeout == openai_pydantic.DEFAULT_TIMEOUT
    assert openai_pydantic.completions._client.timeout == openai_pydantic.DEFAULT_TIMEOUT

    openai_pydantic.timeout = 3

    assert openai_pydantic.timeout == 3
    assert openai_pydantic.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert openai_pydantic.max_retries == openai_pydantic.DEFAULT_MAX_RETRIES
    assert openai_pydantic.completions._client.max_retries == openai_pydantic.DEFAULT_MAX_RETRIES

    openai_pydantic.max_retries = 1

    assert openai_pydantic.max_retries == 1
    assert openai_pydantic.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert openai_pydantic.default_headers == None

    openai_pydantic.default_headers = {"Foo": "Bar"}

    assert openai_pydantic.default_headers["Foo"] == "Bar"
    assert openai_pydantic.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert openai_pydantic.default_query is None
    assert openai_pydantic.completions._client._custom_query == {}

    openai_pydantic.default_query = {"Foo": {"nested": 1}}

    assert openai_pydantic.default_query["Foo"] == {"nested": 1}
    assert openai_pydantic.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert openai_pydantic.http_client is None

    original_http_client = openai_pydantic.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    openai_pydantic.http_client = new_client

    assert openai_pydantic.completions._client._client is new_client


import contextlib
from typing import Iterator

from openai_pydantic.lib.azure import AzureOpenAI


@contextlib.contextmanager
def fresh_env() -> Iterator[None]:
    old = _os.environ.copy()

    try:
        _os.environ.clear()
        yield
    finally:
        _os.environ.clear()
        _os.environ.update(old)


def test_only_api_key_results_in_openai_pydantic_api() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        openai_pydantic.api_key = "example API key"

        assert type(openai_pydantic.completions._client).__name__ == "_ModuleClient"


def test_azure_api_key_env_without_api_version() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"

        with pytest.raises(
            ValueError,
            match=r"Must provide either the `api_version` argument or the `OPENAI_API_VERSION` environment variable",
        ):
            openai_pydantic.completions._client  # noqa: B018


def test_azure_api_key_and_version_env() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"

        with pytest.raises(
            ValueError,
            match=r"Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_OPENAI_ENDPOINT` environment variable",
        ):
            openai_pydantic.completions._client  # noqa: B018


def test_azure_api_key_version_and_endpoint_env() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        openai_pydantic.completions._client  # noqa: B018

        assert openai_pydantic.api_type == "azure"


def test_azure_azure_ad_token_version_and_endpoint_env() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        _os.environ["AZURE_OPENAI_AD_TOKEN"] = "example AD token"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        client = openai_pydantic.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        openai_pydantic.api_type = None
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"
        openai_pydantic.azure_ad_token_provider = lambda: "token"

        client = openai_pydantic.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
