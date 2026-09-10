"""Tests for inspection requests and inspection statuses resources."""

from __future__ import annotations

import datetime

import respx
from httpx import Response

from digna_sdk import DignaClient
from digna_sdk.models import StableInspectionOperationStatus, StableInspectionRequestMode

from .conftest import BASE_URL


@respx.mock
def test_submit_inspection_request(client: DignaClient) -> None:
    route = respx.post(f"{BASE_URL}/v1/inspection-requests").mock(
        return_value=Response(200, json={"id": 42})
    )

    result = client.inspection_requests.submit(
        project_id=1,
        data_source_ids=[5],
        start_date=datetime.date(2026, 1, 1),
        end_date=datetime.date(2026, 1, 31),
        mode=StableInspectionRequestMode.DAILY,
    )

    assert route.called
    assert result.id == 42


@respx.mock
def test_get_inspection_request_status(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/inspection-requests/42").mock(
        return_value=Response(200, json={"id": 42, "status": "COMPLETED"})
    )

    status = client.inspection_requests.get_status(42)

    assert status.status == StableInspectionOperationStatus.COMPLETED


@respx.mock
def test_dataset_inspection_statuses(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/inspection-statuses/data-sets").mock(
        return_value=Response(
            200,
            json=[
                {
                    "project": {"id": 1, "name": "Sales"},
                    "data_source": {"id": 5, "name": "orders_table"},
                    "dataset": {"id": 7, "name": "daily_orders", "full_name": "daily_orders_full"},
                    "dataset_definition": {"id": 3, "name": "daily"},
                    "status": 1,
                    "valid_date": "2026-01-15",
                    "data_volume_status": {"row_count": 120, "status": 1},
                }
            ],
        )
    )

    statuses = client.inspection_statuses.for_datasets(
        5,
        start_date=datetime.date(2026, 1, 1),
        end_date=datetime.date(2026, 1, 31),
    )

    assert len(statuses) == 1
    assert statuses[0].data_volume_status is not None
    assert statuses[0].data_volume_status.row_count == 120
