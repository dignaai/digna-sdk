"""Convenience access to `/v1/data-sets`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.data_sets import (
    create_data_set,
    delete_data_set,
    get_data_set,
    get_data_sets,
    update_data_set,
)
from .._generated.client import AuthenticatedClient, Client
from .._generated.models.create_data_set_request import CreateDataSetRequest
from .._generated.models.stable_data_set_kind import StableDataSetKind
from .._generated.models.update_data_set_request import UpdateDataSetRequest
from .._generated.types import UNSET
from ..models import DataSet


class DataSetsResource:
    """Resource client for `/v1/data-sets`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, data_source_id: int, *, limit: int | None = None) -> list[DataSet]:
        """List datasets belonging to a data source.

        Args:
            data_source_id: Filter by data source ID.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_data_sets.sync_detailed(
            client=self._client,
            data_source_id=data_source_id,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(DataSet, unwrap(response))

    def get(self, dataset_id: int) -> DataSet:
        """Get a single dataset by id.

        Args:
            dataset_id: Data set ID.
        """
        response = get_data_set.sync_detailed(client=self._client, dataset_id=dataset_id)
        return to_model(DataSet, unwrap(response))

    def create(
        self,
        *,
        data_source_id: int,
        name: str,
        kind: StableDataSetKind,
        filter_expression: str = "",
        grouping_expression: str = "",
    ) -> DataSet:
        """Create a new dataset.

        Args:
            data_source_id: The data source this dataset is derived from.
            name: Data set name.
            kind: Whether the dataset is static, dynamic, or hybrid.
            filter_expression: Row filter expression applied to the data source.
            grouping_expression: Grouping expression used to split the data source into datasets.
        """
        body = CreateDataSetRequest(
            data_source_id=data_source_id,
            name=name,
            kind=kind,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
        )
        response = create_data_set.sync_detailed(client=self._client, body=body)
        return to_model(DataSet, unwrap(response))

    def update(
        self,
        dataset_id: int,
        *,
        name: str,
        kind: StableDataSetKind,
        filter_expression: str = "",
        grouping_expression: str = "",
    ) -> DataSet:
        """Update an existing dataset.

        Args:
            dataset_id: Data set ID.
            name: Data set name.
            kind: Whether the dataset is static, dynamic, or hybrid.
            filter_expression: Row filter expression applied to the data source.
            grouping_expression: Grouping expression used to split the data source into datasets.
        """
        body = UpdateDataSetRequest(
            name=name,
            kind=kind,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
        )
        response = update_data_set.sync_detailed(client=self._client, dataset_id=dataset_id, body=body)
        return to_model(DataSet, unwrap(response))

    def delete(self, dataset_id: int) -> None:
        """Delete a dataset.

        Args:
            dataset_id: Data set ID.
        """
        response = delete_data_set.sync_detailed(client=self._client, dataset_id=dataset_id)
        unwrap(response)
