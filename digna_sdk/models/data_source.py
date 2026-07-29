from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_data_source_kind import StableDataSourceKind
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_db_connection import DataSourceDbConnection
  from ..models.data_source_modules import DataSourceModules
  from ..models.data_source_object import DataSourceObject
  from ..models.data_source_project import DataSourceProject





T = TypeVar("T", bound="DataSource")



@_attrs_define
class DataSource:
    """Model for DataSource.
    
    Attributes:
        db_connection (DataSourceDbConnection, required=True): No description
        id (int, required=True): No description
        kind (StableDataSourceKind, required=True): No description
        modules (DataSourceModules, required=True): No description
        name (str, required=True): No description
        object (DataSourceObject, required=True): No description
        project (DataSourceProject, required=True): No description
        report_empty_datasets (bool, required=True): No description
        snapshot_filter (str, required=True): No description
        snapshot_query (str, required=True): No description
    """

    db_connection: DataSourceDbConnection
    id: int
    kind: StableDataSourceKind
    modules: DataSourceModules
    name: str
    object_: DataSourceObject
    project: DataSourceProject
    report_empty_datasets: bool
    snapshot_filter: str
    snapshot_query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_db_connection import DataSourceDbConnection
        from ..models.data_source_modules import DataSourceModules
        from ..models.data_source_object import DataSourceObject
        from ..models.data_source_project import DataSourceProject
        db_connection = self.db_connection.to_dict()

        id = self.id

        kind = self.kind.value

        modules = self.modules.to_dict()

        name = self.name

        object_ = self.object_.to_dict()

        project = self.project.to_dict()

        report_empty_datasets = self.report_empty_datasets

        snapshot_filter = self.snapshot_filter

        snapshot_query = self.snapshot_query


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "db_connection": db_connection,
            "id": id,
            "kind": kind,
            "modules": modules,
            "name": name,
            "object": object_,
            "project": project,
            "report_empty_datasets": report_empty_datasets,
            "snapshot_filter": snapshot_filter,
            "snapshot_query": snapshot_query,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_db_connection import DataSourceDbConnection
        from ..models.data_source_modules import DataSourceModules
        from ..models.data_source_object import DataSourceObject
        from ..models.data_source_project import DataSourceProject
        d = dict(src_dict)
        db_connection = DataSourceDbConnection.from_dict(d.pop("db_connection"))




        id = d.pop("id")

        kind = StableDataSourceKind(d.pop("kind"))




        modules = DataSourceModules.from_dict(d.pop("modules"))




        name = d.pop("name")

        object_ = DataSourceObject.from_dict(d.pop("object"))




        project = DataSourceProject.from_dict(d.pop("project"))




        report_empty_datasets = d.pop("report_empty_datasets")

        snapshot_filter = d.pop("snapshot_filter")

        snapshot_query = d.pop("snapshot_query")

        data_source = cls(
            db_connection=db_connection,
            id=id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            project=project,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )


        data_source.additional_properties = d
        return data_source

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
