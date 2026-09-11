"""The main entry point for the Digna SDK."""

from __future__ import annotations

import httpx

from ._generated.client import AuthenticatedClient, Client
from .resources import (
    AttributesResource,
    CheckDefinitionsResource,
    DataSetsResource,
    DataSourcesResource,
    DbConnectionsResource,
    InspectionRequestsResource,
    InspectionStatusesResource,
    ProjectsResource,
)


class DignaClient:
    """Pythonic client for the Digna stable API.

    Example:
        ```python
        from digna_sdk import DignaClient

        client = DignaClient(base_url="http://localhost:8000", token="<api-token>")
        for project in client.projects.list():
            print(project.id, project.name)
        ```
    """

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        timeout: float | httpx.Timeout | None = 30.0,
        verify_ssl: bool | str = True,
    ) -> None:
        timeout_obj = timeout if isinstance(timeout, httpx.Timeout) or timeout is None else httpx.Timeout(timeout)
        self._client: AuthenticatedClient | Client = AuthenticatedClient(
            base_url=base_url.rstrip("/"),
            token=token,
            timeout=timeout_obj,
            verify_ssl=verify_ssl,
        )

        self.projects = ProjectsResource(self._client)
        self.data_sources = DataSourcesResource(self._client)
        self.data_sets = DataSetsResource(self._client)
        self.attributes = AttributesResource(self._client)
        self.check_definitions = CheckDefinitionsResource(self._client)
        self.db_connections = DbConnectionsResource(self._client)
        self.inspection_requests = InspectionRequestsResource(self._client)
        self.inspection_statuses = InspectionStatusesResource(self._client)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._client.get_httpx_client().close()

    def __enter__(self) -> DignaClient:
        self._client.__enter__()
        return self

    def __exit__(self, *args: object) -> None:
        self._client.__exit__(*args)
