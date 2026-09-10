"""Convenience access to `/v1/projects`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.projects import get_project, get_projects
from .._generated.client import AuthenticatedClient, Client
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
