from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.attribute_check_definition_statistic import AttributeCheckDefinitionStatistic





T = TypeVar("T", bound="AttributeCheckDefinition")



@_attrs_define
class AttributeCheckDefinition:
    """Model for AttributeCheckDefinition.
    
    Attributes:
        id (int, required=True): No description
        statistic (AttributeCheckDefinitionStatistic, required=True): No description
    """

    id: int
    statistic: AttributeCheckDefinitionStatistic
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_check_definition_statistic import AttributeCheckDefinitionStatistic
        id = self.id

        statistic = self.statistic.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "statistic": statistic,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_check_definition_statistic import AttributeCheckDefinitionStatistic
        d = dict(src_dict)
        id = d.pop("id")

        statistic = AttributeCheckDefinitionStatistic.from_dict(d.pop("statistic"))




        attribute_check_definition = cls(
            id=id,
            statistic=statistic,
        )


        attribute_check_definition.additional_properties = d
        return attribute_check_definition

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
