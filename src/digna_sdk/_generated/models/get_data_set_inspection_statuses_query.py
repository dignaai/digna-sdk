from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="GetDataSetInspectionStatusesQuery")


@_attrs_define
class GetDataSetInspectionStatusesQuery:
    """
    Attributes:
        data_source_id (int):
        end_date (datetime.date):
        start_date (datetime.date):
        data_analytics_status (int | None | Unset):
        data_anomaly_status (int | None | Unset):
        data_validation_status (int | None | Unset):
        data_volume_status (int | None | Unset):
        dataset_id (int | None | Unset):
        inspection_status (int | None | Unset):
        limit (int | None | Unset):
    """

    data_source_id: int
    end_date: datetime.date
    start_date: datetime.date
    data_analytics_status: int | None | Unset = UNSET
    data_anomaly_status: int | None | Unset = UNSET
    data_validation_status: int | None | Unset = UNSET
    data_volume_status: int | None | Unset = UNSET
    dataset_id: int | None | Unset = UNSET
    inspection_status: int | None | Unset = UNSET
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_source_id = self.data_source_id

        end_date = self.end_date.isoformat()

        start_date = self.start_date.isoformat()

        data_analytics_status: int | None | Unset
        if isinstance(self.data_analytics_status, Unset):
            data_analytics_status = UNSET
        else:
            data_analytics_status = self.data_analytics_status

        data_anomaly_status: int | None | Unset
        if isinstance(self.data_anomaly_status, Unset):
            data_anomaly_status = UNSET
        else:
            data_anomaly_status = self.data_anomaly_status

        data_validation_status: int | None | Unset
        if isinstance(self.data_validation_status, Unset):
            data_validation_status = UNSET
        else:
            data_validation_status = self.data_validation_status

        data_volume_status: int | None | Unset
        if isinstance(self.data_volume_status, Unset):
            data_volume_status = UNSET
        else:
            data_volume_status = self.data_volume_status

        dataset_id: int | None | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = self.dataset_id

        inspection_status: int | None | Unset
        if isinstance(self.inspection_status, Unset):
            inspection_status = UNSET
        else:
            inspection_status = self.inspection_status

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source_id": data_source_id,
                "end_date": end_date,
                "start_date": start_date,
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
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if inspection_status is not UNSET:
            field_dict["inspection_status"] = inspection_status
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_source_id = d.pop("data_source_id")

        end_date = datetime.date.fromisoformat(d.pop("end_date"))

        start_date = datetime.date.fromisoformat(d.pop("start_date"))

        def _parse_data_analytics_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_analytics_status = _parse_data_analytics_status(d.pop("data_analytics_status", UNSET))

        def _parse_data_anomaly_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_anomaly_status = _parse_data_anomaly_status(d.pop("data_anomaly_status", UNSET))

        def _parse_data_validation_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_validation_status = _parse_data_validation_status(
            d.pop("data_validation_status", UNSET)
        )

        def _parse_data_volume_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_volume_status = _parse_data_volume_status(d.pop("data_volume_status", UNSET))

        def _parse_dataset_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dataset_id = _parse_dataset_id(d.pop("dataset_id", UNSET))

        def _parse_inspection_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inspection_status = _parse_inspection_status(d.pop("inspection_status", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        get_data_set_inspection_statuses_query = cls(
            data_source_id=data_source_id,
            end_date=end_date,
            start_date=start_date,
            data_analytics_status=data_analytics_status,
            data_anomaly_status=data_anomaly_status,
            data_validation_status=data_validation_status,
            data_volume_status=data_volume_status,
            dataset_id=dataset_id,
            inspection_status=inspection_status,
            limit=limit,
        )

        get_data_set_inspection_statuses_query.additional_properties = d
        return get_data_set_inspection_statuses_query

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
