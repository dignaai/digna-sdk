from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_data_source_kind import StableDataSourceKind
from ..models.stable_data_source_query_mode import StableDataSourceQueryMode
from typing import cast

if TYPE_CHECKING:
    from ..models.data_source_modules import DataSourceModules
    from ..models.data_source_object import DataSourceObject


T = TypeVar("T", bound="UpdateDataSourceRequest")


@_attrs_define
class UpdateDataSourceRequest:
    """
    Attributes:
        db_connection_id (int):
        kind (StableDataSourceKind):
        modules (DataSourceModules):
        name (str):
        object_ (DataSourceObject):
        query_mode (StableDataSourceQueryMode):
        report_empty_datasets (bool):
        snapshot_filter (str):
        snapshot_query (str):
    """

    db_connection_id: int
    kind: StableDataSourceKind
    modules: DataSourceModules
    name: str
    object_: DataSourceObject
    query_mode: StableDataSourceQueryMode
    report_empty_datasets: bool
    snapshot_filter: str
    snapshot_query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_modules import DataSourceModules  # noqa: PLC0415
        from ..models.data_source_object import DataSourceObject  # noqa: PLC0415

        db_connection_id = self.db_connection_id

        kind = self.kind.value

        modules = self.modules.to_dict()

        name = self.name

        object_ = self.object_.to_dict()

        query_mode = self.query_mode.value

        report_empty_datasets = self.report_empty_datasets

        snapshot_filter = self.snapshot_filter

        snapshot_query = self.snapshot_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "db_connection_id": db_connection_id,
                "kind": kind,
                "modules": modules,
                "name": name,
                "object": object_,
                "query_mode": query_mode,
                "report_empty_datasets": report_empty_datasets,
                "snapshot_filter": snapshot_filter,
                "snapshot_query": snapshot_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_modules import DataSourceModules  # noqa: PLC0415
        from ..models.data_source_object import DataSourceObject  # noqa: PLC0415

        d = dict(src_dict)
        db_connection_id = d.pop("db_connection_id")

        kind = StableDataSourceKind(d.pop("kind"))

        modules = DataSourceModules.from_dict(d.pop("modules"))

        name = d.pop("name")

        object_ = DataSourceObject.from_dict(d.pop("object"))

        query_mode = StableDataSourceQueryMode(d.pop("query_mode"))

        report_empty_datasets = d.pop("report_empty_datasets")

        snapshot_filter = d.pop("snapshot_filter")

        snapshot_query = d.pop("snapshot_query")

        update_data_source_request = cls(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            query_mode=query_mode,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )

        update_data_source_request.additional_properties = d
        return update_data_source_request

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
