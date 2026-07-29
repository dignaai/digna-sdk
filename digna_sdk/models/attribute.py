from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_attribute_category import StableAttributeCategory
from typing import cast

if TYPE_CHECKING:
  from ..models.attribute_check_definition import AttributeCheckDefinition
  from ..models.attribute_data_source import AttributeDataSource
  from ..models.attribute_project import AttributeProject





T = TypeVar("T", bound="Attribute")



@_attrs_define
class Attribute:
    """Model for Attribute.
    
    Attributes:
        category (StableAttributeCategory, required=True): No description
        check_definitions (list[AttributeCheckDefinition], required=True): No description
        data_source (AttributeDataSource, required=True): No description
        data_type (str, required=True): No description
        id (int, required=True): No description
        name (str, required=True): No description
        project (AttributeProject, required=True): No description
    """

    category: StableAttributeCategory
    check_definitions: list[AttributeCheckDefinition]
    data_source: AttributeDataSource
    data_type: str
    id: int
    name: str
    project: AttributeProject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_check_definition import AttributeCheckDefinition
        from ..models.attribute_data_source import AttributeDataSource
        from ..models.attribute_project import AttributeProject
        category = self.category.value

        check_definitions = []
        for check_definitions_item_data in self.check_definitions:
            check_definitions_item = check_definitions_item_data.to_dict()
            check_definitions.append(check_definitions_item)



        data_source = self.data_source.to_dict()

        data_type = self.data_type

        id = self.id

        name = self.name

        project = self.project.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
            "check_definitions": check_definitions,
            "data_source": data_source,
            "data_type": data_type,
            "id": id,
            "name": name,
            "project": project,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_check_definition import AttributeCheckDefinition
        from ..models.attribute_data_source import AttributeDataSource
        from ..models.attribute_project import AttributeProject
        d = dict(src_dict)
        category = StableAttributeCategory(d.pop("category"))




        check_definitions = []
        _check_definitions = d.pop("check_definitions")
        for check_definitions_item_data in (_check_definitions):
            check_definitions_item = AttributeCheckDefinition.from_dict(check_definitions_item_data)



            check_definitions.append(check_definitions_item)


        data_source = AttributeDataSource.from_dict(d.pop("data_source"))




        data_type = d.pop("data_type")

        id = d.pop("id")

        name = d.pop("name")

        project = AttributeProject.from_dict(d.pop("project"))




        attribute = cls(
            category=category,
            check_definitions=check_definitions,
            data_source=data_source,
            data_type=data_type,
            id=id,
            name=name,
            project=project,
        )


        attribute.additional_properties = d
        return attribute

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
