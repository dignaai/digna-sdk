"""Tests for the projects resource and general error handling."""

from __future__ import annotations

import respx
from httpx import Response

from digna_sdk import DignaAuthenticationError, DignaClient, DignaNotFoundError
from digna_sdk.models import Project

from .conftest import BASE_URL


@respx.mock
def test_list_projects(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects").mock(
        return_value=Response(
            200,
            json=[
                {
                    "id": 1,
                    "name": "Sales",
                    "description": "Sales project",
                    "db_connections": [{"id": 10, "name": "warehouse"}],
                }
            ],
        )
    )

    projects = client.projects.list()

    assert projects == [
        Project(
            id=1,
            name="Sales",
            description="Sales project",
            db_connections=[{"id": 10, "name": "warehouse"}],  # type: ignore[list-item]
        )
    ]


@respx.mock
def test_get_project(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects/1").mock(
        return_value=Response(
            200,
            json={"id": 1, "name": "Sales", "description": "", "db_connections": []},
        )
    )

    project = client.projects.get(1)

    assert project.id == 1
    assert project.name == "Sales"


@respx.mock
def test_authentication_error(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects").mock(
        return_value=Response(
            401, json={"code": "NOT_AUTHENTICATED", "message": "Invalid API key"}
        )
    )

    try:
        client.projects.list()
    except DignaAuthenticationError as exc:
        assert exc.status_code == 401
        assert exc.message == "Invalid API key"
    else:
        raise AssertionError("Expected DignaAuthenticationError")


@respx.mock
def test_not_found_error(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/projects/999").mock(
        return_value=Response(404, json={"code": "NOT_FOUND", "message": "Project not found"})
    )

    try:
        client.projects.get(999)
    except DignaNotFoundError as exc:
        assert exc.status_code == 404
    else:
        raise AssertionError("Expected DignaNotFoundError")
