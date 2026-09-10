"""Submit an inspection request, wait for it to finish, then retrieve the results.

This is the typical "run an inspection and get results" flow:

    1. Submit an inspection request for one or more data sources on a given day.
    2. Poll `get_status` (via `wait_until_finished`) until it reaches a terminal state.
    3. Once finished, retrieve the resulting inspection statuses for the data
       source(s) and their datasets.

Run with the SDK's virtual environment active, e.g.:

    .venv\\Scripts\\python.exe examples\\inspection_flow.py

Configure via environment variables, or edit the defaults below:

    DIGNA_BASE_URL       e.g. http://localhost:8000
    DIGNA_API_TOKEN      your API token
    DIGNA_PROJECT_ID     e.g. 63
    DIGNA_DATA_SOURCE_ID e.g. 77
    DIGNA_INSPECTION_DATE e.g. 2026-08-31
"""

from __future__ import annotations

import datetime
import os

from digna_sdk import DignaAPIError, DignaClient, DignaInspectionRequestFailed
from digna_sdk.models import StableInspectionRequestMode


def main() -> None:
    base_url = os.environ.get("DIGNA_BASE_URL", "http://localhost:8000")
    token = os.environ.get("DIGNA_API_TOKEN", "")
    project_id = int(os.environ.get("DIGNA_PROJECT_ID", "63"))
    data_source_id = int(os.environ.get("DIGNA_DATA_SOURCE_ID", "77"))
    inspection_date = datetime.date.fromisoformat(
        os.environ.get("DIGNA_INSPECTION_DATE", "2026-08-31")
    )

    with DignaClient(base_url=base_url, token=token) as client:
        # 1. Submit the inspection request.
        request = client.inspection_requests.submit(
            project_id=project_id,
            data_source_ids=[data_source_id],
            start_date=inspection_date,
            end_date=inspection_date,
            mode=StableInspectionRequestMode.DAILY,
        )
        print(f"Submitted inspection request #{request.id}")

        # 2. Wait for it to finish (raises on FAILED/ABORTED/CANCELLED, or on timeout).
        try:
            final_status = client.inspection_requests.wait_until_finished(
                request.id, poll_interval=2.0, timeout=300.0
            )
            print(f"Inspection request #{request.id} finished: {final_status.status.value}")
        except DignaInspectionRequestFailed as exc:
            print(f"Inspection request #{request.id} did not succeed: {exc.status.value}")
        except TimeoutError as exc:
            print(exc)
            return

        # 3. Retrieve the resulting statuses, regardless of outcome.
        data_source_statuses = client.inspection_statuses.for_data_sources(
            data_source_id=data_source_id,
            start_date=inspection_date,
            end_date=inspection_date,
        )
        for status in data_source_statuses:
            print(
                f"Data source #{status.data_source.id} on {status.valid_date}: "
                f"status={status.status.name}, row_count={status.row_count}"
            )

        dataset_statuses = client.inspection_statuses.for_datasets(
            data_source_id,
            start_date=inspection_date,
            end_date=inspection_date,
        )
        for status in dataset_statuses:
            print(
                f"Dataset '{status.dataset.full_name}' on {status.valid_date}: "
                f"status={status.status.name}"
            )


if __name__ == "__main__":
    try:
        main()
    except DignaAPIError as exc:
        print(f"API error {exc.status_code}: {exc.message}")
