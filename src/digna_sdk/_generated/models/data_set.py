from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_data_set_kind import StableDataSetKind
from typing import cast

if TYPE_CHECKING:
    from ..models.data_set_data_source import DataSetDataSource
    from ..models.data_set_project import DataSetProject


T = TypeVar("T", bound="DataSet")


@_attrs_define
class DataSet:
    """
    Attributes:
        data_source (DataSetDataSource):
        filter_expression (str):
        grouping_expression (str):
        id (int):
        kind (StableDataSetKind):
        name (str):
        project (DataSetProject):
    """

    data_source: DataSetDataSource
    filter_expression: str
    grouping_expression: str
    id: int
    kind: StableDataSetKind
    name: str
    project: DataSetProject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_set_data_source import DataSetDataSource  # noqa: PLC0415
        from ..models.data_set_project import DataSetProject  # noqa: PLC0415

        data_source = self.data_source.to_dict()

        filter_expression = self.filter_expression

        grouping_expression = self.grouping_expression

        id = self.id

        kind = self.kind.value

        name = self.name

        project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source": data_source,
                "filter_expression": filter_expression,
                "grouping_expression": grouping_expression,
                "id": id,
                "kind": kind,
                "name": name,
                "project": project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_set_data_source import DataSetDataSource  # noqa: PLC0415
        from ..models.data_set_project import DataSetProject  # noqa: PLC0415

        d = dict(src_dict)
        data_source = DataSetDataSource.from_dict(d.pop("data_source"))

        filter_expression = d.pop("filter_expression")

        grouping_expression = d.pop("grouping_expression")

        id = d.pop("id")

        kind = StableDataSetKind(d.pop("kind"))

        name = d.pop("name")

        project = DataSetProject.from_dict(d.pop("project"))

        data_set = cls(
            data_source=data_source,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            id=id,
            kind=kind,
            name=name,
            project=project,
        )

        data_set.additional_properties = d
        return data_set

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
