from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DataSourceModules")



@_attrs_define
class DataSourceModules:
    """Model for DataSourceModules.
    
    Attributes:
        data_analytics (bool, required=True): No description
        data_anomaly (bool, required=True): No description
        data_validation (bool, required=True): No description
        schema_tracker (bool, required=True): No description
        timeliness (bool, required=True): No description
    """

    data_analytics: bool
    data_anomaly: bool
    data_validation: bool
    schema_tracker: bool
    timeliness: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_analytics = self.data_analytics

        data_anomaly = self.data_anomaly

        data_validation = self.data_validation

        schema_tracker = self.schema_tracker

        timeliness = self.timeliness


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data_analytics": data_analytics,
            "data_anomaly": data_anomaly,
            "data_validation": data_validation,
            "schema_tracker": schema_tracker,
            "timeliness": timeliness,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_analytics = d.pop("data_analytics")

        data_anomaly = d.pop("data_anomaly")

        data_validation = d.pop("data_validation")

        schema_tracker = d.pop("schema_tracker")

        timeliness = d.pop("timeliness")

        data_source_modules = cls(
            data_analytics=data_analytics,
            data_anomaly=data_anomaly,
            data_validation=data_validation,
            schema_tracker=schema_tracker,
            timeliness=timeliness,
        )


        data_source_modules.additional_properties = d
        return data_source_modules

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
