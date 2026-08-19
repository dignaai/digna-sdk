from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stable_inspection_request_mode import StableInspectionRequestMode
from ..models.stable_inspection_request_weekday import StableInspectionRequestWeekday
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SubmitInspectionRequest")



@_attrs_define
class SubmitInspectionRequest:
    """Model for SubmitInspectionRequest.
    
    Attributes:
        data_source_ids (list[int], required=True): No description
        end_date (str, required=True): No description
        include_all_data_sources (bool, required=True): No description
        inspection_job_id (Any, required=False): No description
        mode (StableInspectionRequestMode, required=True): No description
        monthly_mode_days (list[int], required=True): No description
        project_id (int, required=True): No description
        start_date (str, required=True): No description
        use_notification (bool, required=True): No description
        weekly_mode_weekdays (list[StableInspectionRequestWeekday], required=True): No description
    """

    data_source_ids: list[int]
    end_date: datetime.date
    include_all_data_sources: bool
    mode: StableInspectionRequestMode
    monthly_mode_days: list[int]
    project_id: int
    start_date: datetime.date
    use_notification: bool
    weekly_mode_weekdays: list[StableInspectionRequestWeekday]
    inspection_job_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_source_ids = self.data_source_ids



        end_date = self.end_date.isoformat()

        include_all_data_sources = self.include_all_data_sources

        mode = self.mode.value

        monthly_mode_days = self.monthly_mode_days



        project_id = self.project_id

        start_date = self.start_date.isoformat()

        use_notification = self.use_notification

        weekly_mode_weekdays = []
        for weekly_mode_weekdays_item_data in self.weekly_mode_weekdays:
            weekly_mode_weekdays_item = weekly_mode_weekdays_item_data.value
            weekly_mode_weekdays.append(weekly_mode_weekdays_item)



        inspection_job_id: int | None | Unset
        if isinstance(self.inspection_job_id, Unset):
            inspection_job_id = UNSET
        else:
            inspection_job_id = self.inspection_job_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data_source_ids": data_source_ids,
            "end_date": end_date,
            "include_all_data_sources": include_all_data_sources,
            "mode": mode,
            "monthly_mode_days": monthly_mode_days,
            "project_id": project_id,
            "start_date": start_date,
            "use_notification": use_notification,
            "weekly_mode_weekdays": weekly_mode_weekdays,
        })
        if inspection_job_id is not UNSET:
            field_dict["inspection_job_id"] = inspection_job_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_source_ids = cast(list[int], d.pop("data_source_ids"))


        end_date = datetime.date.fromisoformat(d.pop("end_date"))




        include_all_data_sources = d.pop("include_all_data_sources")

        mode = StableInspectionRequestMode(d.pop("mode"))




        monthly_mode_days = cast(list[int], d.pop("monthly_mode_days"))


        project_id = d.pop("project_id")

        start_date = datetime.date.fromisoformat(d.pop("start_date"))




        use_notification = d.pop("use_notification")

        weekly_mode_weekdays = []
        _weekly_mode_weekdays = d.pop("weekly_mode_weekdays")
        for weekly_mode_weekdays_item_data in (_weekly_mode_weekdays):
            weekly_mode_weekdays_item = StableInspectionRequestWeekday(weekly_mode_weekdays_item_data)



            weekly_mode_weekdays.append(weekly_mode_weekdays_item)


        def _parse_inspection_job_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inspection_job_id = _parse_inspection_job_id(d.pop("inspection_job_id", UNSET))


        submit_inspection_request = cls(
            data_source_ids=data_source_ids,
            end_date=end_date,
            include_all_data_sources=include_all_data_sources,
            mode=mode,
            monthly_mode_days=monthly_mode_days,
            project_id=project_id,
            start_date=start_date,
            use_notification=use_notification,
            weekly_mode_weekdays=weekly_mode_weekdays,
            inspection_job_id=inspection_job_id,
        )


        submit_inspection_request.additional_properties = d
        return submit_inspection_request

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
