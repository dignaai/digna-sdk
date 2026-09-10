"""Tests for InspectionRequestsResource.wait_until_finished."""

from __future__ import annotations

import datetime

import pytest
import respx
from httpx import Response

from digna_sdk import DignaClient, DignaInspectionRequestFailed
from digna_sdk.models import StableInspectionRequestMode

from .conftest import BASE_URL


@respx.mock
def test_wait_until_finished_success(client: DignaClient) -> None:
    respx.post(f"{BASE_URL}/v1/inspection-requests").mock(
        return_value=Response(200, json={"id": 1})
    )
    statuses = iter(["PENDING", "RUNNING", "COMPLETED"])
    respx.get(f"{BASE_URL}/v1/inspection-requests/1").mock(
        side_effect=lambda request: Response(200, json={"id": 1, "status": next(statuses)})
    )

    request = client.inspection_requests.submit(
        project_id=63,
        data_source_ids=[77],
        start_date=datetime.date(2026, 8, 31),
        end_date=datetime.date(2026, 8, 31),
        mode=StableInspectionRequestMode.DAILY,
    )
    final_status = client.inspection_requests.wait_until_finished(request.id, poll_interval=0)

    assert final_status.status.value == "COMPLETED"


@respx.mock
def test_wait_until_finished_raises_on_failure(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/inspection-requests/1").mock(
        return_value=Response(200, json={"id": 1, "status": "FAILED"})
    )

    with pytest.raises(DignaInspectionRequestFailed) as exc_info:
        client.inspection_requests.wait_until_finished(1, poll_interval=0)

    assert exc_info.value.inspection_request_id == 1


@respx.mock
def test_wait_until_finished_times_out(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/inspection-requests/1").mock(
        return_value=Response(200, json={"id": 1, "status": "RUNNING"})
    )

    with pytest.raises(TimeoutError):
        client.inspection_requests.wait_until_finished(1, poll_interval=0, timeout=0)
