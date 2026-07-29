from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_data_set_kind import StableDataSetKind






T = TypeVar("T", bound="CreateDataSetRequest")



@_attrs_define
class CreateDataSetRequest:
    """Model for CreateDataSetRequest.
    
    Attributes:
        data_source_id (int, required=True): No description
        filter_expression (str, required=True): No description
        grouping_expression (str, required=True): No description
        kind (StableDataSetKind, required=True): No description
        name (str, required=True): No description
    """

    data_source_id: int
    filter_expression: str
    grouping_expression: str
    kind: StableDataSetKind
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_source_id = self.data_source_id

        filter_expression = self.filter_expression

        grouping_expression = self.grouping_expression

        kind = self.kind.value

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data_source_id": data_source_id,
            "filter_expression": filter_expression,
            "grouping_expression": grouping_expression,
            "kind": kind,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_source_id = d.pop("data_source_id")

        filter_expression = d.pop("filter_expression")

        grouping_expression = d.pop("grouping_expression")

        kind = StableDataSetKind(d.pop("kind"))




        name = d.pop("name")

        create_data_set_request = cls(
            data_source_id=data_source_id,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )


        create_data_set_request.additional_properties = d
        return create_data_set_request

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
