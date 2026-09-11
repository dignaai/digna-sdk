from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_status import TestStatus


T = TypeVar("T", bound="DatasetInspectionStatusDataAnomalyStatus")


@_attrs_define
class DatasetInspectionStatusDataAnomalyStatus:
    """
    Attributes:
        num_checks (int):
        num_failed (int):
        num_passed (int):
        num_uncertain (int):
        status (TestStatus):
    """

    num_checks: int
    num_failed: int
    num_passed: int
    num_uncertain: int
    status: TestStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_checks = self.num_checks

        num_failed = self.num_failed

        num_passed = self.num_passed

        num_uncertain = self.num_uncertain

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "num_checks": num_checks,
                "num_failed": num_failed,
                "num_passed": num_passed,
                "num_uncertain": num_uncertain,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_checks = d.pop("num_checks")

        num_failed = d.pop("num_failed")

        num_passed = d.pop("num_passed")

        num_uncertain = d.pop("num_uncertain")

        status = TestStatus(d.pop("status"))

        dataset_inspection_status_data_anomaly_status = cls(
            num_checks=num_checks,
            num_failed=num_failed,
            num_passed=num_passed,
            num_uncertain=num_uncertain,
            status=status,
        )

        dataset_inspection_status_data_anomaly_status.additional_properties = d
        return dataset_inspection_status_data_anomaly_status

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
