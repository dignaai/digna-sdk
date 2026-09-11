"""Convenience access to `/v1/data-sources`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.data_sources import (
    create_data_source,
    delete_data_source,
    get_data_source,
    get_data_sources,
    update_data_source,
)
from .._generated.client import AuthenticatedClient, Client
from .._generated.models.create_data_source_request import CreateDataSourceRequest
from .._generated.models.data_source_modules import DataSourceModules as _GeneratedModules
from .._generated.models.data_source_object import DataSourceObject as _GeneratedObject
from .._generated.models.stable_data_source_kind import StableDataSourceKind
from .._generated.models.stable_data_source_query_mode import StableDataSourceQueryMode
from .._generated.models.update_data_source_request import UpdateDataSourceRequest
from .._generated.types import UNSET
from ..models import DataSource, DataSourceModules, DataSourceObject


class DataSourcesResource:
    """Resource client for `/v1/data-sources`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, project_id: int, *, limit: int | None = None) -> list[DataSource]:
        """List data sources belonging to a project.

        Args:
            project_id: Filter by project ID.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_data_sources.sync_detailed(
            client=self._client,
            project_id=project_id,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(DataSource, unwrap(response))

    def get(self, data_source_id: int) -> DataSource:
        """Get a single data source by id.

        Args:
            data_source_id: Data source ID.
        """
        response = get_data_source.sync_detailed(client=self._client, data_source_id=data_source_id)
        return to_model(DataSource, unwrap(response))

    def create(
        self,
        *,
        project_id: int,
        db_connection_id: int,
        name: str,
        kind: StableDataSourceKind,
        query_mode: StableDataSourceQueryMode,
        object: DataSourceObject,
        modules: DataSourceModules,
        report_empty_datasets: bool = False,
        snapshot_filter: str = "",
        snapshot_query: str = "",
    ) -> DataSource:
        """Create a new data source.

        Args:
            project_id: The project this data source belongs to.
            db_connection_id: The database connection used to query the source table/view.
            name: Data source name.
            kind: Whether the source is a table, view, or query.
            query_mode: Whether snapshots are queried individually or combined.
            object: The catalog/schema/table location of the source data.
            modules: Which inspection modules are enabled for this data source.
            report_empty_datasets: Whether to still report datasets that hold no rows.
            snapshot_filter: Row filter expression used to select a snapshot.
            snapshot_query: Custom query used instead of `object` when `kind` is `QUERY`.
        """
        body = CreateDataSourceRequest(
            project_id=project_id,
            db_connection_id=db_connection_id,
            name=name,
            kind=kind,
            query_mode=query_mode,
            object_=_GeneratedObject(**object.model_dump()),
            modules=_GeneratedModules(**modules.model_dump()),
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = create_data_source.sync_detailed(client=self._client, body=body)
        return to_model(DataSource, unwrap(response))

    def update(
        self,
        data_source_id: int,
        *,
        db_connection_id: int,
        name: str,
        kind: StableDataSourceKind,
        query_mode: StableDataSourceQueryMode,
        object: DataSourceObject,
        modules: DataSourceModules,
        report_empty_datasets: bool = False,
        snapshot_filter: str = "",
        snapshot_query: str = "",
    ) -> DataSource:
        """Update an existing data source.

        Args:
            data_source_id: Data source ID.
            db_connection_id: The database connection used to query the source table/view.
            name: Data source name.
            kind: Whether the source is a table, view, or query.
            query_mode: Whether snapshots are queried individually or combined.
            object: The catalog/schema/table location of the source data.
            modules: Which inspection modules are enabled for this data source.
            report_empty_datasets: Whether to still report datasets that hold no rows.
            snapshot_filter: Row filter expression used to select a snapshot.
            snapshot_query: Custom query used instead of `object` when `kind` is `QUERY`.
        """
        body = UpdateDataSourceRequest(
            db_connection_id=db_connection_id,
            name=name,
            kind=kind,
            query_mode=query_mode,
            object_=_GeneratedObject(**object.model_dump()),
            modules=_GeneratedModules(**modules.model_dump()),
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = update_data_source.sync_detailed(
            client=self._client, data_source_id=data_source_id, body=body
        )
        return to_model(DataSource, unwrap(response))

    def delete(self, data_source_id: int) -> None:
        """Delete a data source.

        Args:
            data_source_id: Data source ID.
        """
        response = delete_data_source.sync_detailed(
            client=self._client, data_source_id=data_source_id
        )
        unwrap(response)
