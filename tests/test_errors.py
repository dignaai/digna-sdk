"""Tests that low-level HTTP failures surface as SDK exceptions."""

from __future__ import annotations

import httpx
import pytest
import respx
from httpx import Response

import digna_sdk
from digna_sdk import (
    DignaAPIError,
    DignaAuthenticationError,
    DignaClient,
    DignaConnectionError,
)

from .conftest import BASE_URL


@respx.mock
def test_list_sends_limit(client: DignaClient) -> None:
    route = respx.get(f"{BASE_URL}/v1/projects", params={"limit": "1"}).mock(
        return_value=Response(200, json=[])
    )

    client.projects.list(limit=1)

    assert route.called


@pytest.mark.parametrize("error", [httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout])
@respx.mock
def test_transport_errors_are_wrapped(client: DignaClient, error: type[Exception]) -> None:
    respx.get(f"{BASE_URL}/v1/projects").mock(side_effect=error)

    with pytest.raises(DignaConnectionError) as exc_info:
        client.projects.list()

    assert isinstance(exc_info.value.__cause__, error)


@respx.mock
def test_html_response_raises_api_error(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects").mock(
        return_value=Response(200, html="<!doctype html><html></html>")
    )

    with pytest.raises(DignaAPIError) as exc_info:
        client.projects.list()

    assert exc_info.value.status_code == 200
    assert "base_url" in exc_info.value.message


@respx.mock
def test_plain_text_error_keeps_body_and_status_mapping(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects").mock(
        return_value=Response(401, text="Unauthorized")
    )

    with pytest.raises(DignaAuthenticationError) as exc_info:
        client.projects.list()

    assert exc_info.value.message == "Unauthorized"


@respx.mock
def test_empty_body_is_accepted(client: DignaClient) -> None:
    respx.delete(f"{BASE_URL}/v1/attributes/9").mock(return_value=Response(204))

    client.attributes.delete(9)


@pytest.mark.parametrize("token", ["", "   "])
def test_empty_token_is_rejected(token: str) -> None:
    with pytest.raises(ValueError):
        DignaClient(base_url=BASE_URL, token=token)


@respx.mock
def test_token_is_sent_as_bearer() -> None:
    route = respx.get(f"{BASE_URL}/v1/projects").mock(return_value=Response(200, json=[]))

    DignaClient(base_url=BASE_URL, token=" secret\n").projects.list()

    assert route.calls.last.request.headers["Authorization"] == "Bearer secret"


def test_version_matches_package_metadata() -> None:
    from importlib.metadata import version

    assert digna_sdk.__version__ == version("digna-sdk")
