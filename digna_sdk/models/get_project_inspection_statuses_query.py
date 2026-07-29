from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetProjectInspectionStatusesQuery")



@_attrs_define
class GetProjectInspectionStatusesQuery:
    """Model for GetProjectInspectionStatusesQuery.
    
    Attributes:
        end_date (str, required=True): No description
        limit (Any, required=False): No description
        project_id (int, required=True): No description
        start_date (str, required=True): No description
    """

    end_date: datetime.date
    project_id: int
    start_date: datetime.date
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.isoformat()

        project_id = self.project_id

        start_date = self.start_date.isoformat()

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "end_date": end_date,
            "project_id": project_id,
            "start_date": start_date,
        })
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_date = datetime.date.fromisoformat(d.pop("end_date"))




        project_id = d.pop("project_id")

        start_date = datetime.date.fromisoformat(d.pop("start_date"))




        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))


        get_project_inspection_statuses_query = cls(
            end_date=end_date,
            project_id=project_id,
            start_date=start_date,
            limit=limit,
        )


        get_project_inspection_statuses_query.additional_properties = d
        return get_project_inspection_statuses_query

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
