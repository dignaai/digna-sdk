"""Convenience access to `/v1/check-definitions`."""

from __future__ import annotations

from .._convert import to_model_list, unwrap
from .._generated.api.check_definitions import get_check_definitions
from .._generated.client import AuthenticatedClient, Client
from .._generated.types import UNSET
from ..models import CheckDefinition


class CheckDefinitionsResource:
    """Resource client for `/v1/check-definitions`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, data_source_id: int, *, limit: int | None = None) -> list[CheckDefinition]:
        """List check definitions belonging to a data source.

        Args:
            data_source_id: Filter by data source ID.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_check_definitions.sync_detailed(
            client=self._client,
            data_source_id=data_source_id,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(CheckDefinition, unwrap(response))
