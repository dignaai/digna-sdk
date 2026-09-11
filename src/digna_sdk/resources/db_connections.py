"""Convenience access to `/v1/db-connections`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.db_connections import get_db_connection, get_db_connections
from .._generated.client import AuthenticatedClient, Client
from .._generated.types import UNSET
from ..models import DbConnection


class DbConnectionsResource:
    """Resource client for `/v1/db-connections`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, *, limit: int | None = None) -> list[DbConnection]:
        """List all database connections.

        Args:
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_db_connections.sync_detailed(
            client=self._client,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(DbConnection, unwrap(response))

    def get(self, db_connection_id: int) -> DbConnection:
        """Get a single database connection by id.

        Args:
            db_connection_id: Db connection ID.
        """
        response = get_db_connection.sync_detailed(
            client=self._client, db_connection_id=db_connection_id
        )
        return to_model(DbConnection, unwrap(response))
