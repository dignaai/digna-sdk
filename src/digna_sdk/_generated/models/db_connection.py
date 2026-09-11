from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_db_connection_profiling_mode import StableDbConnectionProfilingMode
from ..models.stable_db_connection_technology import StableDbConnectionTechnology


T = TypeVar("T", bound="DbConnection")


@_attrs_define
class DbConnection:
    """
    Attributes:
        id (int):
        name (str):
        profiling_mode (StableDbConnectionProfilingMode):
        technology (StableDbConnectionTechnology):
        work_schema (str):
    """

    id: int
    name: str
    profiling_mode: StableDbConnectionProfilingMode
    technology: StableDbConnectionTechnology
    work_schema: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        profiling_mode = self.profiling_mode.value

        technology = self.technology.value

        work_schema = self.work_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "profiling_mode": profiling_mode,
                "technology": technology,
                "work_schema": work_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        profiling_mode = StableDbConnectionProfilingMode(d.pop("profiling_mode"))

        technology = StableDbConnectionTechnology(d.pop("technology"))

        work_schema = d.pop("work_schema")

        db_connection = cls(
            id=id,
            name=name,
            profiling_mode=profiling_mode,
            technology=technology,
            work_schema=work_schema,
        )

        db_connection.additional_properties = d
        return db_connection

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
