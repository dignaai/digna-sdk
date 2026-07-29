from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_definition_attribute import CheckDefinitionAttribute
  from ..models.check_definition_data_source import CheckDefinitionDataSource
  from ..models.check_definition_project import CheckDefinitionProject
  from ..models.check_definition_statistic import CheckDefinitionStatistic





T = TypeVar("T", bound="CheckDefinition")



@_attrs_define
class CheckDefinition:
    """Model for CheckDefinition.
    
    Attributes:
        attribute (Any, required=False): No description
        data_anomaly_enabled (bool, required=True): No description
        data_source (CheckDefinitionDataSource, required=True): No description
        id (int, required=True): No description
        lower_limit (Any, required=False): No description
        max_threshold (Any, required=False): No description
        min_threshold (Any, required=False): No description
        project (CheckDefinitionProject, required=True): No description
        statistic (CheckDefinitionStatistic, required=True): No description
        upper_limit (Any, required=False): No description
    """

    data_anomaly_enabled: bool
    data_source: CheckDefinitionDataSource
    id: int
    project: CheckDefinitionProject
    statistic: CheckDefinitionStatistic
    attribute: CheckDefinitionAttribute | None | Unset = UNSET
    lower_limit: float | None | Unset = UNSET
    max_threshold: float | None | Unset = UNSET
    min_threshold: float | None | Unset = UNSET
    upper_limit: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_definition_attribute import CheckDefinitionAttribute
        from ..models.check_definition_data_source import CheckDefinitionDataSource
        from ..models.check_definition_project import CheckDefinitionProject
        from ..models.check_definition_statistic import CheckDefinitionStatistic
        data_anomaly_enabled = self.data_anomaly_enabled

        data_source = self.data_source.to_dict()

        id = self.id

        project = self.project.to_dict()

        statistic = self.statistic.to_dict()

        attribute: dict[str, Any] | None | Unset
        if isinstance(self.attribute, Unset):
            attribute = UNSET
        elif isinstance(self.attribute, CheckDefinitionAttribute):
            attribute = self.attribute.to_dict()
        else:
            attribute = self.attribute

        lower_limit: float | None | Unset
        if isinstance(self.lower_limit, Unset):
            lower_limit = UNSET
        else:
            lower_limit = self.lower_limit

        max_threshold: float | None | Unset
        if isinstance(self.max_threshold, Unset):
            max_threshold = UNSET
        else:
            max_threshold = self.max_threshold

        min_threshold: float | None | Unset
        if isinstance(self.min_threshold, Unset):
            min_threshold = UNSET
        else:
            min_threshold = self.min_threshold

        upper_limit: float | None | Unset
        if isinstance(self.upper_limit, Unset):
            upper_limit = UNSET
        else:
            upper_limit = self.upper_limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data_anomaly_enabled": data_anomaly_enabled,
            "data_source": data_source,
            "id": id,
            "project": project,
            "statistic": statistic,
        })
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if lower_limit is not UNSET:
            field_dict["lower_limit"] = lower_limit
        if max_threshold is not UNSET:
            field_dict["max_threshold"] = max_threshold
        if min_threshold is not UNSET:
            field_dict["min_threshold"] = min_threshold
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_definition_attribute import CheckDefinitionAttribute
        from ..models.check_definition_data_source import CheckDefinitionDataSource
        from ..models.check_definition_project import CheckDefinitionProject
        from ..models.check_definition_statistic import CheckDefinitionStatistic
        d = dict(src_dict)
        data_anomaly_enabled = d.pop("data_anomaly_enabled")

        data_source = CheckDefinitionDataSource.from_dict(d.pop("data_source"))




        id = d.pop("id")

        project = CheckDefinitionProject.from_dict(d.pop("project"))




        statistic = CheckDefinitionStatistic.from_dict(d.pop("statistic"))




        def _parse_attribute(data: object) -> CheckDefinitionAttribute | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attribute_type_1 = CheckDefinitionAttribute.from_dict(data)



                return attribute_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckDefinitionAttribute | None | Unset, data)

        attribute = _parse_attribute(d.pop("attribute", UNSET))


        def _parse_lower_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lower_limit = _parse_lower_limit(d.pop("lower_limit", UNSET))


        def _parse_max_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_threshold = _parse_max_threshold(d.pop("max_threshold", UNSET))


        def _parse_min_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_threshold = _parse_min_threshold(d.pop("min_threshold", UNSET))


        def _parse_upper_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upper_limit = _parse_upper_limit(d.pop("upper_limit", UNSET))


        check_definition = cls(
            data_anomaly_enabled=data_anomaly_enabled,
            data_source=data_source,
            id=id,
            project=project,
            statistic=statistic,
            attribute=attribute,
            lower_limit=lower_limit,
            max_threshold=max_threshold,
            min_threshold=min_threshold,
            upper_limit=upper_limit,
        )


        check_definition.additional_properties = d
        return check_definition

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
