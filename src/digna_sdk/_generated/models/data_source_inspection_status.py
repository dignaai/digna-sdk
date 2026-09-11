from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.inspection_status import InspectionStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.data_source_inspection_status_data_analytics_data_source_status import (
        DataSourceInspectionStatusDataAnalyticsDataSourceStatus,
    )
    from ..models.data_source_inspection_status_data_anomaly_status import (
        DataSourceInspectionStatusDataAnomalyStatus,
    )
    from ..models.data_source_inspection_status_data_source import (
        DataSourceInspectionStatusDataSource,
    )
    from ..models.data_source_inspection_status_data_validation_status import (
        DataSourceInspectionStatusDataValidationStatus,
    )
    from ..models.data_source_inspection_status_data_volume_status import (
        DataSourceInspectionStatusDataVolumeStatus,
    )
    from ..models.data_source_inspection_status_project import DataSourceInspectionStatusProject


T = TypeVar("T", bound="DataSourceInspectionStatus")


@_attrs_define
class DataSourceInspectionStatus:
    """
    Attributes:
        data_source (DataSourceInspectionStatusDataSource):
        is_inspected (bool):
        project (DataSourceInspectionStatusProject):
        status (InspectionStatus):
        valid_date (datetime.date):
        data_analytics_status (DataSourceInspectionStatusDataAnalyticsDataSourceStatus | None | Unset):
        data_anomaly_status (DataSourceInspectionStatusDataAnomalyStatus | None | Unset):
        data_validation_status (DataSourceInspectionStatusDataValidationStatus | None | Unset):
        data_volume_status (DataSourceInspectionStatusDataVolumeStatus | None | Unset):
        inspected_at (datetime.datetime | None | Unset):
        row_count (int | None | Unset): Rows the data source held on `valid_date`, `None` for a date it was not
            profiled on.
    """

    data_source: DataSourceInspectionStatusDataSource
    is_inspected: bool
    project: DataSourceInspectionStatusProject
    status: InspectionStatus
    valid_date: datetime.date
    data_analytics_status: (
        DataSourceInspectionStatusDataAnalyticsDataSourceStatus | None | Unset
    ) = UNSET
    data_anomaly_status: DataSourceInspectionStatusDataAnomalyStatus | None | Unset = UNSET
    data_validation_status: DataSourceInspectionStatusDataValidationStatus | None | Unset = UNSET
    data_volume_status: DataSourceInspectionStatusDataVolumeStatus | None | Unset = UNSET
    inspected_at: datetime.datetime | None | Unset = UNSET
    row_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_inspection_status_data_analytics_data_source_status import (
            DataSourceInspectionStatusDataAnalyticsDataSourceStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_anomaly_status import (
            DataSourceInspectionStatusDataAnomalyStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_source import (
            DataSourceInspectionStatusDataSource,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_validation_status import (
            DataSourceInspectionStatusDataValidationStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_volume_status import (
            DataSourceInspectionStatusDataVolumeStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_project import DataSourceInspectionStatusProject  # noqa: PLC0415

        data_source = self.data_source.to_dict()

        is_inspected = self.is_inspected

        project = self.project.to_dict()

        status = self.status.value

        valid_date = self.valid_date.isoformat()

        data_analytics_status: dict[str, Any] | None | Unset
        if isinstance(self.data_analytics_status, Unset):
            data_analytics_status = UNSET
        elif isinstance(
            self.data_analytics_status, DataSourceInspectionStatusDataAnalyticsDataSourceStatus
        ):
            data_analytics_status = self.data_analytics_status.to_dict()
        else:
            data_analytics_status = self.data_analytics_status

        data_anomaly_status: dict[str, Any] | None | Unset
        if isinstance(self.data_anomaly_status, Unset):
            data_anomaly_status = UNSET
        elif isinstance(self.data_anomaly_status, DataSourceInspectionStatusDataAnomalyStatus):
            data_anomaly_status = self.data_anomaly_status.to_dict()
        else:
            data_anomaly_status = self.data_anomaly_status

        data_validation_status: dict[str, Any] | None | Unset
        if isinstance(self.data_validation_status, Unset):
            data_validation_status = UNSET
        elif isinstance(
            self.data_validation_status, DataSourceInspectionStatusDataValidationStatus
        ):
            data_validation_status = self.data_validation_status.to_dict()
        else:
            data_validation_status = self.data_validation_status

        data_volume_status: dict[str, Any] | None | Unset
        if isinstance(self.data_volume_status, Unset):
            data_volume_status = UNSET
        elif isinstance(self.data_volume_status, DataSourceInspectionStatusDataVolumeStatus):
            data_volume_status = self.data_volume_status.to_dict()
        else:
            data_volume_status = self.data_volume_status

        inspected_at: None | str | Unset
        if isinstance(self.inspected_at, Unset):
            inspected_at = UNSET
        elif isinstance(self.inspected_at, datetime.datetime):
            inspected_at = self.inspected_at.isoformat()
        else:
            inspected_at = self.inspected_at

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source": data_source,
                "is_inspected": is_inspected,
                "project": project,
                "status": status,
                "valid_date": valid_date,
            }
        )
        if data_analytics_status is not UNSET:
            field_dict["data_analytics_status"] = data_analytics_status
        if data_anomaly_status is not UNSET:
            field_dict["data_anomaly_status"] = data_anomaly_status
        if data_validation_status is not UNSET:
            field_dict["data_validation_status"] = data_validation_status
        if data_volume_status is not UNSET:
            field_dict["data_volume_status"] = data_volume_status
        if inspected_at is not UNSET:
            field_dict["inspected_at"] = inspected_at
        if row_count is not UNSET:
            field_dict["row_count"] = row_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_inspection_status_data_analytics_data_source_status import (
            DataSourceInspectionStatusDataAnalyticsDataSourceStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_anomaly_status import (
            DataSourceInspectionStatusDataAnomalyStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_source import (
            DataSourceInspectionStatusDataSource,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_validation_status import (
            DataSourceInspectionStatusDataValidationStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_data_volume_status import (
            DataSourceInspectionStatusDataVolumeStatus,
        )  # noqa: PLC0415
        from ..models.data_source_inspection_status_project import DataSourceInspectionStatusProject  # noqa: PLC0415

        d = dict(src_dict)
        data_source = DataSourceInspectionStatusDataSource.from_dict(d.pop("data_source"))

        is_inspected = d.pop("is_inspected")

        project = DataSourceInspectionStatusProject.from_dict(d.pop("project"))

        status = InspectionStatus(d.pop("status"))

        valid_date = datetime.date.fromisoformat(d.pop("valid_date"))

        def _parse_data_analytics_status(
            data: object,
        ) -> DataSourceInspectionStatusDataAnalyticsDataSourceStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_analytics_status_type_1 = (
                    DataSourceInspectionStatusDataAnalyticsDataSourceStatus.from_dict(data)
                )

                return data_analytics_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DataSourceInspectionStatusDataAnalyticsDataSourceStatus | None | Unset, data
            )

        data_analytics_status = _parse_data_analytics_status(d.pop("data_analytics_status", UNSET))

        def _parse_data_anomaly_status(
            data: object,
        ) -> DataSourceInspectionStatusDataAnomalyStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_anomaly_status_type_1 = DataSourceInspectionStatusDataAnomalyStatus.from_dict(
                    data
                )

                return data_anomaly_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataSourceInspectionStatusDataAnomalyStatus | None | Unset, data)

        data_anomaly_status = _parse_data_anomaly_status(d.pop("data_anomaly_status", UNSET))

        def _parse_data_validation_status(
            data: object,
        ) -> DataSourceInspectionStatusDataValidationStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_validation_status_type_1 = (
                    DataSourceInspectionStatusDataValidationStatus.from_dict(data)
                )

                return data_validation_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataSourceInspectionStatusDataValidationStatus | None | Unset, data)

        data_validation_status = _parse_data_validation_status(
            d.pop("data_validation_status", UNSET)
        )

        def _parse_data_volume_status(
            data: object,
        ) -> DataSourceInspectionStatusDataVolumeStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_volume_status_type_1 = DataSourceInspectionStatusDataVolumeStatus.from_dict(
                    data
                )

                return data_volume_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataSourceInspectionStatusDataVolumeStatus | None | Unset, data)

        data_volume_status = _parse_data_volume_status(d.pop("data_volume_status", UNSET))

        def _parse_inspected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inspected_at_type_0 = datetime.datetime.fromisoformat(data)

                return inspected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        inspected_at = _parse_inspected_at(d.pop("inspected_at", UNSET))

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        data_source_inspection_status = cls(
            data_source=data_source,
            is_inspected=is_inspected,
            project=project,
            status=status,
            valid_date=valid_date,
            data_analytics_status=data_analytics_status,
            data_anomaly_status=data_anomaly_status,
            data_validation_status=data_validation_status,
            data_volume_status=data_volume_status,
            inspected_at=inspected_at,
            row_count=row_count,
        )

        data_source_inspection_status.additional_properties = d
        return data_source_inspection_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
