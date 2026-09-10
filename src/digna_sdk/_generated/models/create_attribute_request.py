from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_attribute_category import StableAttributeCategory
from typing import cast


T = TypeVar("T", bound="CreateAttributeRequest")


@_attrs_define
class CreateAttributeRequest:
    """
    Attributes:
        category (StableAttributeCategory):
        data_source_id (int):
        data_type (str):
        name (str):
        statistic_ids (list[int]):
    """

    category: StableAttributeCategory
    data_source_id: int
    data_type: str
    name: str
    statistic_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        data_source_id = self.data_source_id

        data_type = self.data_type

        name = self.name

        statistic_ids = self.statistic_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "data_source_id": data_source_id,
                "data_type": data_type,
                "name": name,
                "statistic_ids": statistic_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = StableAttributeCategory(d.pop("category"))

        data_source_id = d.pop("data_source_id")

        data_type = d.pop("data_type")

        name = d.pop("name")

        statistic_ids = cast(list[int], d.pop("statistic_ids"))

        create_attribute_request = cls(
            category=category,
            data_source_id=data_source_id,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )

        create_attribute_request.additional_properties = d
        return create_attribute_request

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
