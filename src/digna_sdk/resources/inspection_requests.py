"""Convenience access to `/v1/inspection-requests`."""

from __future__ import annotations

import datetime
import time

from .._convert import to_model, unwrap
from .._generated.api.inspection_requests import get_inspection_request, submit_inspection_request
from .._generated.client import AuthenticatedClient, Client
from .._generated.models.stable_inspection_request_mode import StableInspectionRequestMode
from .._generated.models.stable_inspection_request_weekday import StableInspectionRequestWeekday
from .._generated.models.submit_inspection_request import (
    SubmitInspectionRequest as _GeneratedSubmitInspectionRequest,
)
from .._generated.types import UNSET
from ..exceptions import DignaInspectionRequestFailed
from ..models import (
    InspectionRequestStatus,
    StableInspectionOperationStatus,
    SubmittedInspectionRequest,
)

_TERMINAL_STATUSES = {
    StableInspectionOperationStatus.COMPLETED,
    StableInspectionOperationStatus.FAILED,
    StableInspectionOperationStatus.ABORTED,
    StableInspectionOperationStatus.CANCELLED,
}


class InspectionRequestsResource:
    """Resource client for `/v1/inspection-requests`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def submit(
        self,
        *,
        project_id: int,
        data_source_ids: list[int],
        start_date: datetime.date,
        end_date: datetime.date,
        mode: StableInspectionRequestMode,
        include_all_data_sources: bool = False,
        use_notification: bool = False,
        monthly_mode_days: list[int] | None = None,
        weekly_mode_weekdays: list[StableInspectionRequestWeekday] | None = None,
        inspection_job_id: int | None = None,
    ) -> SubmittedInspectionRequest:
        """Submit a new inspection request for a project's data sources.

        Args:
            project_id: The project the data sources belong to.
            data_source_ids: IDs of the data sources to inspect. Ignored when
                `include_all_data_sources` is `True`.
            start_date: First date to inspect (inclusive).
            end_date: Last date to inspect (inclusive).
            mode: How the requested date range should be scheduled (daily, weekly, monthly).
            include_all_data_sources: Inspect every data source in the project instead of
                just `data_source_ids`.
            use_notification: Whether to send notifications for this request.
            monthly_mode_days: Days of the month to run on, when `mode` is `MONTHLY`.
            weekly_mode_weekdays: Weekdays to run on, when `mode` is `WEEKLY`.
            inspection_job_id: Optional ID linking this request to an existing inspection job.
        """
        body = _GeneratedSubmitInspectionRequest(
            project_id=project_id,
            data_source_ids=data_source_ids,
            start_date=start_date,
            end_date=end_date,
            mode=mode,
            include_all_data_sources=include_all_data_sources,
            use_notification=use_notification,
            monthly_mode_days=monthly_mode_days or [],
            weekly_mode_weekdays=weekly_mode_weekdays or [],
            inspection_job_id=inspection_job_id if inspection_job_id is not None else UNSET,
        )
        response = submit_inspection_request.sync_detailed(client=self._client, body=body)
        return to_model(SubmittedInspectionRequest, unwrap(response))

    def get_status(self, inspection_request_id: int) -> InspectionRequestStatus:
        """Poll the status of a previously submitted inspection request.

        Args:
            inspection_request_id: Inspection request ID.
        """
        response = get_inspection_request.sync_detailed(
            client=self._client, inspection_request_id=inspection_request_id
        )
        return to_model(InspectionRequestStatus, unwrap(response))

    def wait_until_finished(
        self,
        inspection_request_id: int,
        *,
        poll_interval: float = 2.0,
        timeout: float = 300.0,
    ) -> InspectionRequestStatus:
        """Repeatedly call `get_status` until the request reaches a terminal state.

        Args:
            inspection_request_id: Inspection request ID, as returned by `submit`.
            poll_interval: Seconds to sleep between status checks.
            timeout: Maximum seconds to wait before giving up.

        Raises:
            DignaInspectionRequestFailed: if the request ends as FAILED, ABORTED, or CANCELLED.
            TimeoutError: if `timeout` seconds elapse before a terminal state is reached.
        """
        deadline = time.monotonic() + timeout
        while True:
            status = self.get_status(inspection_request_id)
            if status.status in _TERMINAL_STATUSES:
                if status.status != StableInspectionOperationStatus.COMPLETED:
                    raise DignaInspectionRequestFailed(inspection_request_id, status.status)
                return status
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"Inspection request {inspection_request_id} did not finish within "
                    f"{timeout}s (last status: {status.status.value})"
                )
            time.sleep(poll_interval)
