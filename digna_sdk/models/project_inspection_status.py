from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.inspection_status import InspectionStatus
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.project_inspection_status_project import ProjectInspectionStatusProject





T = TypeVar("T", bound="ProjectInspectionStatus")



@_attrs_define
class ProjectInspectionStatus:
    """Model for ProjectInspectionStatus.
    
    Attributes:
        project (ProjectInspectionStatusProject, required=True): No description
        status (InspectionStatus, required=True): No description
        valid_date (str, required=True): No description
    """

    project: ProjectInspectionStatusProject
    status: InspectionStatus
    valid_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_inspection_status_project import ProjectInspectionStatusProject
        project = self.project.to_dict()

        status = self.status.value

        valid_date = self.valid_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project": project,
            "status": status,
            "valid_date": valid_date,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_inspection_status_project import ProjectInspectionStatusProject
        d = dict(src_dict)
        project = ProjectInspectionStatusProject.from_dict(d.pop("project"))




        status = InspectionStatus(d.pop("status"))




        valid_date = datetime.date.fromisoformat(d.pop("valid_date"))




        project_inspection_status = cls(
            project=project,
            status=status,
            valid_date=valid_date,
        )


        project_inspection_status.additional_properties = d
        return project_inspection_status

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
