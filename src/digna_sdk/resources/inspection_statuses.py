"""Convenience access to `/v1/inspection-statuses/*`."""

from __future__ import annotations

import datetime

from .._convert import to_model_list, unwrap
from .._generated.api.inspection_statuses import (
    get_data_set_inspection_statuses,
    get_data_source_inspection_statuses,
    get_project_inspection_statuses,
)
from .._generated.client import AuthenticatedClient, Client
from .._generated.types import UNSET
from ..models import (
    DatasetInspectionStatus,
    DataSourceInspectionStatus,
    InspectionStatus,
    ProjectInspectionStatus,
    TestStatus,
)


class InspectionStatusesResource:
    """Resource client for `/v1/inspection-statuses/*`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def for_projects(
        self,
        project_id: int,
        *,
        start_date: datetime.date,
        end_date: datetime.date,
        limit: int | None = None,
    ) -> list[ProjectInspectionStatus]:
        """Get daily inspection statuses for a project.

        Args:
            project_id: Project ID.
            start_date: Start date (inclusive).
            end_date: End date (inclusive).
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_project_inspection_statuses.sync_detailed(
            client=self._client,
            project_id=project_id,
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(ProjectInspectionStatus, unwrap(response))

    def for_data_sources(
        self,
        *,
        start_date: datetime.date,
        end_date: datetime.date,
        project_id: int | None = None,
        data_source_id: int | None = None,
        data_source_name_like: str | None = None,
        is_inspected: bool | None = None,
        data_volume_status: TestStatus | None = None,
        data_anomaly_status: TestStatus | None = None,
        data_validation_status: TestStatus | None = None,
        data_analytics_status: TestStatus | None = None,
        inspection_status: InspectionStatus | None = None,
        limit: int | None = None,
    ) -> list[DataSourceInspectionStatus]:
        """Get daily inspection statuses for one or all data sources.

        Args:
            start_date: Start date (inclusive).
            end_date: End date (inclusive).
            project_id: Filter by project ID.
            data_source_id: Filter by data source ID.
            data_source_name_like: Filter by data source name.
            is_inspected: Filter by inspected state.
            data_volume_status: Filter by data volume status.
            data_anomaly_status: Filter by data anomaly status.
            data_validation_status: Filter by data validation status.
            data_analytics_status: Filter by data analytics status.
            inspection_status: Filter by overall inspection status.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_data_source_inspection_statuses.sync_detailed(
            client=self._client,
            project_id=project_id if project_id is not None else UNSET,
            data_source_id=data_source_id if data_source_id is not None else UNSET,
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            data_source_name_like=(
                data_source_name_like if data_source_name_like is not None else UNSET
            ),
            is_inspected=is_inspected if is_inspected is not None else UNSET,
            data_volume_status=(
                int(data_volume_status) if data_volume_status is not None else UNSET
            ),
            data_anomaly_status=(
                int(data_anomaly_status) if data_anomaly_status is not None else UNSET
            ),
            data_validation_status=(
                int(data_validation_status) if data_validation_status is not None else UNSET
            ),
            data_analytics_status=(
                int(data_analytics_status) if data_analytics_status is not None else UNSET
            ),
            inspection_status=int(inspection_status) if inspection_status is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(DataSourceInspectionStatus, unwrap(response))

    def for_datasets(
        self,
        data_source_id: int,
        *,
        start_date: datetime.date,
        end_date: datetime.date,
        dataset_id: int | None = None,
        data_volume_status: TestStatus | None = None,
        data_anomaly_status: TestStatus | None = None,
        data_validation_status: TestStatus | None = None,
        data_analytics_status: TestStatus | None = None,
        inspection_status: InspectionStatus | None = None,
        limit: int | None = None,
    ) -> list[DatasetInspectionStatus]:
        """Get daily inspection statuses for one or all datasets of a data source.

        Args:
            data_source_id: Filter by data source ID.
            start_date: Start date (inclusive).
            end_date: End date (inclusive).
            dataset_id: Filter by data set ID.
            data_volume_status: Filter by data volume status.
            data_anomaly_status: Filter by data anomaly status.
            data_validation_status: Filter by data validation status.
            data_analytics_status: Filter by data analytics status.
            inspection_status: Filter by overall inspection status.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_data_set_inspection_statuses.sync_detailed(
            client=self._client,
            data_source_id=data_source_id,
            dataset_id=dataset_id if dataset_id is not None else UNSET,
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            data_volume_status=(
                int(data_volume_status) if data_volume_status is not None else UNSET
            ),
            data_anomaly_status=(
                int(data_anomaly_status) if data_anomaly_status is not None else UNSET
            ),
            data_validation_status=(
                int(data_validation_status) if data_validation_status is not None else UNSET
            ),
            data_analytics_status=(
                int(data_analytics_status) if data_analytics_status is not None else UNSET
            ),
            inspection_status=int(inspection_status) if inspection_status is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(DatasetInspectionStatus, unwrap(response))
