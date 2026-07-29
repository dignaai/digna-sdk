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
  from ..models.dataset_inspection_status_data_analytics_status import DatasetInspectionStatusDataAnalyticsStatus
  from ..models.dataset_inspection_status_data_anomaly_status import DatasetInspectionStatusDataAnomalyStatus
  from ..models.dataset_inspection_status_data_source import DatasetInspectionStatusDataSource
  from ..models.dataset_inspection_status_data_validation_status import DatasetInspectionStatusDataValidationStatus
  from ..models.dataset_inspection_status_data_volume_status import DatasetInspectionStatusDataVolumeStatus
  from ..models.dataset_inspection_status_dataset import DatasetInspectionStatusDataset
  from ..models.dataset_inspection_status_dataset_definition import DatasetInspectionStatusDatasetDefinition
  from ..models.dataset_inspection_status_project import DatasetInspectionStatusProject





T = TypeVar("T", bound="DatasetInspectionStatus")



@_attrs_define
class DatasetInspectionStatus:
    """Model for DatasetInspectionStatus.
    
    Attributes:
        data_analytics_status (Any, required=False): No description
        data_anomaly_status (Any, required=False): No description
        data_source (DatasetInspectionStatusDataSource, required=True): No description
        data_validation_status (Any, required=False): No description
        data_volume_status (Any, required=False): No description
        dataset (DatasetInspectionStatusDataset, required=True): No description
        dataset_definition (DatasetInspectionStatusDatasetDefinition, required=True): No description
        project (DatasetInspectionStatusProject, required=True): No description
        status (InspectionStatus, required=True): No description
        valid_date (str, required=True): No description
    """

    data_source: DatasetInspectionStatusDataSource
    dataset: DatasetInspectionStatusDataset
    dataset_definition: DatasetInspectionStatusDatasetDefinition
    project: DatasetInspectionStatusProject
    status: InspectionStatus
    valid_date: datetime.date
    data_analytics_status: DatasetInspectionStatusDataAnalyticsStatus | None | Unset = UNSET
    data_anomaly_status: DatasetInspectionStatusDataAnomalyStatus | None | Unset = UNSET
    data_validation_status: DatasetInspectionStatusDataValidationStatus | None | Unset = UNSET
    data_volume_status: DatasetInspectionStatusDataVolumeStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_inspection_status_data_analytics_status import DatasetInspectionStatusDataAnalyticsStatus
        from ..models.dataset_inspection_status_data_anomaly_status import DatasetInspectionStatusDataAnomalyStatus
        from ..models.dataset_inspection_status_data_source import DatasetInspectionStatusDataSource
        from ..models.dataset_inspection_status_data_validation_status import DatasetInspectionStatusDataValidationStatus
        from ..models.dataset_inspection_status_data_volume_status import DatasetInspectionStatusDataVolumeStatus
        from ..models.dataset_inspection_status_dataset import DatasetInspectionStatusDataset
        from ..models.dataset_inspection_status_dataset_definition import DatasetInspectionStatusDatasetDefinition
        from ..models.dataset_inspection_status_project import DatasetInspectionStatusProject
        data_source = self.data_source.to_dict()

        dataset = self.dataset.to_dict()

        dataset_definition = self.dataset_definition.to_dict()

        project = self.project.to_dict()

        status = self.status.value

        valid_date = self.valid_date.isoformat()

        data_analytics_status: dict[str, Any] | None | Unset
        if isinstance(self.data_analytics_status, Unset):
            data_analytics_status = UNSET
        elif isinstance(self.data_analytics_status, DatasetInspectionStatusDataAnalyticsStatus):
            data_analytics_status = self.data_analytics_status.to_dict()
        else:
            data_analytics_status = self.data_analytics_status

        data_anomaly_status: dict[str, Any] | None | Unset
        if isinstance(self.data_anomaly_status, Unset):
            data_anomaly_status = UNSET
        elif isinstance(self.data_anomaly_status, DatasetInspectionStatusDataAnomalyStatus):
            data_anomaly_status = self.data_anomaly_status.to_dict()
        else:
            data_anomaly_status = self.data_anomaly_status

        data_validation_status: dict[str, Any] | None | Unset
        if isinstance(self.data_validation_status, Unset):
            data_validation_status = UNSET
        elif isinstance(self.data_validation_status, DatasetInspectionStatusDataValidationStatus):
            data_validation_status = self.data_validation_status.to_dict()
        else:
            data_validation_status = self.data_validation_status

        data_volume_status: dict[str, Any] | None | Unset
        if isinstance(self.data_volume_status, Unset):
            data_volume_status = UNSET
        elif isinstance(self.data_volume_status, DatasetInspectionStatusDataVolumeStatus):
            data_volume_status = self.data_volume_status.to_dict()
        else:
            data_volume_status = self.data_volume_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data_source": data_source,
            "dataset": dataset,
            "dataset_definition": dataset_definition,
            "project": project,
            "status": status,
            "valid_date": valid_date,
        })
        if data_analytics_status is not UNSET:
            field_dict["data_analytics_status"] = data_analytics_status
        if data_anomaly_status is not UNSET:
            field_dict["data_anomaly_status"] = data_anomaly_status
        if data_validation_status is not UNSET:
            field_dict["data_validation_status"] = data_validation_status
        if data_volume_status is not UNSET:
            field_dict["data_volume_status"] = data_volume_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_inspection_status_data_analytics_status import DatasetInspectionStatusDataAnalyticsStatus
        from ..models.dataset_inspection_status_data_anomaly_status import DatasetInspectionStatusDataAnomalyStatus
        from ..models.dataset_inspection_status_data_source import DatasetInspectionStatusDataSource
        from ..models.dataset_inspection_status_data_validation_status import DatasetInspectionStatusDataValidationStatus
        from ..models.dataset_inspection_status_data_volume_status import DatasetInspectionStatusDataVolumeStatus
        from ..models.dataset_inspection_status_dataset import DatasetInspectionStatusDataset
        from ..models.dataset_inspection_status_dataset_definition import DatasetInspectionStatusDatasetDefinition
        from ..models.dataset_inspection_status_project import DatasetInspectionStatusProject
        d = dict(src_dict)
        data_source = DatasetInspectionStatusDataSource.from_dict(d.pop("data_source"))




        dataset = DatasetInspectionStatusDataset.from_dict(d.pop("dataset"))




        dataset_definition = DatasetInspectionStatusDatasetDefinition.from_dict(d.pop("dataset_definition"))




        project = DatasetInspectionStatusProject.from_dict(d.pop("project"))




        status = InspectionStatus(d.pop("status"))




        valid_date = datetime.date.fromisoformat(d.pop("valid_date"))




        def _parse_data_analytics_status(data: object) -> DatasetInspectionStatusDataAnalyticsStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_analytics_status_type_1 = DatasetInspectionStatusDataAnalyticsStatus.from_dict(data)



                return data_analytics_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetInspectionStatusDataAnalyticsStatus | None | Unset, data)

        data_analytics_status = _parse_data_analytics_status(d.pop("data_analytics_status", UNSET))


        def _parse_data_anomaly_status(data: object) -> DatasetInspectionStatusDataAnomalyStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_anomaly_status_type_1 = DatasetInspectionStatusDataAnomalyStatus.from_dict(data)



                return data_anomaly_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetInspectionStatusDataAnomalyStatus | None | Unset, data)

        data_anomaly_status = _parse_data_anomaly_status(d.pop("data_anomaly_status", UNSET))


        def _parse_data_validation_status(data: object) -> DatasetInspectionStatusDataValidationStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_validation_status_type_1 = DatasetInspectionStatusDataValidationStatus.from_dict(data)



                return data_validation_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetInspectionStatusDataValidationStatus | None | Unset, data)

        data_validation_status = _parse_data_validation_status(d.pop("data_validation_status", UNSET))


        def _parse_data_volume_status(data: object) -> DatasetInspectionStatusDataVolumeStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_volume_status_type_1 = DatasetInspectionStatusDataVolumeStatus.from_dict(data)



                return data_volume_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetInspectionStatusDataVolumeStatus | None | Unset, data)

        data_volume_status = _parse_data_volume_status(d.pop("data_volume_status", UNSET))


        dataset_inspection_status = cls(
            data_source=data_source,
            dataset=dataset,
            dataset_definition=dataset_definition,
            project=project,
            status=status,
            valid_date=valid_date,
            data_analytics_status=data_analytics_status,
            data_anomaly_status=data_anomaly_status,
            data_validation_status=data_validation_status,
            data_volume_status=data_volume_status,
        )


        dataset_inspection_status.additional_properties = d
        return dataset_inspection_status

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
