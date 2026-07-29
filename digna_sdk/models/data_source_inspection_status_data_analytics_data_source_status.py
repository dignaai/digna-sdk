from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_status import TestStatus






T = TypeVar("T", bound="DataSourceInspectionStatusDataAnalyticsDataSourceStatus")



@_attrs_define
class DataSourceInspectionStatusDataAnalyticsDataSourceStatus:
    """Model for DataSourceInspectionStatusDataAnalyticsDataSourceStatus.
    
    Attributes:
        num_failed (int, required=True): No description
        num_not_relevant (int, required=True): No description
        num_passed (int, required=True): No description
        status (TestStatus, required=True): No description
    """

    num_failed: int
    num_not_relevant: int
    num_passed: int
    status: TestStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        num_failed = self.num_failed

        num_not_relevant = self.num_not_relevant

        num_passed = self.num_passed

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "num_failed": num_failed,
            "num_not_relevant": num_not_relevant,
            "num_passed": num_passed,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_failed = d.pop("num_failed")

        num_not_relevant = d.pop("num_not_relevant")

        num_passed = d.pop("num_passed")

        status = TestStatus(d.pop("status"))




        data_source_inspection_status_data_analytics_data_source_status = cls(
            num_failed=num_failed,
            num_not_relevant=num_not_relevant,
            num_passed=num_passed,
            status=status,
        )


        data_source_inspection_status_data_analytics_data_source_status.additional_properties = d
        return data_source_inspection_status_data_analytics_data_source_status

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
