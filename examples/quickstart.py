"""Example flows for the Digna Python SDK.

This is a placeholder — replace with the real example flows once provided.
Run with the SDK's virtual environment active, e.g.:

    .venv\\Scripts\\python.exe examples\\quickstart.py
"""

from __future__ import annotations

import datetime
import os

from digna_sdk import DignaAPIError, DignaClient
from digna_sdk.models import StableInspectionRequestMode


def main() -> None:
    base_url = os.environ.get("DIGNA_BASE_URL", "http://localhost:8000")
    token = os.environ.get("DIGNA_API_TOKEN", "")

    with DignaClient(base_url=base_url, token=token) as client:
        try:
            projects = client.projects.list()
        except DignaAPIError as exc:
            print(f"Could not list projects: {exc}")
            return

        for project in projects:
            print(f"Project #{project.id}: {project.name}")

            data_sources = client.data_sources.list(project_id=project.id)
            for data_source in data_sources:
                print(f"  Data source #{data_source.id}: {data_source.name}")

        if projects:
            request = client.inspection_requests.submit(
                project_id=projects[0].id,
                data_source_ids=[],
                include_all_data_sources=True,
                start_date=datetime.date.today() - datetime.timedelta(days=7),
                end_date=datetime.date.today(),
                mode=StableInspectionRequestMode.DAILY,
            )
            print("Submitted inspection request:", request.id)


if __name__ == "__main__":
    main()
