"""Convenience access to `/v1/projects`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.projects import (
    create_project,
    delete_project,
    get_project,
    get_projects,
    update_project,
)
from .._generated.client import AuthenticatedClient, Client
from .._generated.models.create_project_request import CreateProjectRequest
from .._generated.models.update_project_request import UpdateProjectRequest
from .._generated.types import UNSET
from ..models import Project


class ProjectsResource:
    """Resource client for `/v1/projects`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, *, limit: int | None = None) -> list[Project]:
        """List all projects.

        Args:
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_projects.sync_detailed(
            client=self._client,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(Project, unwrap(response))

    def get(self, project_id: int) -> Project:
        """Get a single project by id.

        Args:
            project_id: Project ID.
        """
        response = get_project.sync_detailed(client=self._client, project_id=project_id)
        return to_model(Project, unwrap(response))

    def create(self, *, name: str, description: str, db_connection_ids: list[int]) -> Project:
        """Create a new project.

        Args:
            name: Project name.
            description: Project description.
            db_connection_ids: IDs of the database connections available to this project.
        """
        body = CreateProjectRequest(
            name=name, description=description, db_connection_ids=db_connection_ids
        )
        response = create_project.sync_detailed(client=self._client, body=body)
        return to_model(Project, unwrap(response))

    def update(
        self, project_id: int, *, name: str, description: str, db_connection_ids: list[int]
    ) -> Project:
        """Update an existing project.

        Args:
            project_id: Project ID.
            name: Project name.
            description: Project description.
            db_connection_ids: IDs of the database connections available to this project.
        """
        body = UpdateProjectRequest(
            name=name, description=description, db_connection_ids=db_connection_ids
        )
        response = update_project.sync_detailed(client=self._client, project_id=project_id, body=body)
        return to_model(Project, unwrap(response))

    def delete(self, project_id: int) -> None:
        """Delete a project.

        Args:
            project_id: Project ID.
        """
        response = delete_project.sync_detailed(client=self._client, project_id=project_id)
        unwrap(response)
