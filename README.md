# digna_sdk

Python SDK for programmatic access to your Digna instance.

This SDK provides:

- A high-level client with area-based APIs
- Typed request and response models
- Sync and async methods
- Consistent exception handling for API and not-found cases

## Installation

```bash
pip install digna-sdk
```

Requires Python 3.11+.

## Configuration

Set the following environment variables:

```bash
export DIGNA_BASE_URL="https://your-digna-instance.example.com"
export DIGNA_API_TOKEN="your-api-token"
```

PowerShell:

```powershell
$env:DIGNA_BASE_URL = "https://your-digna-instance.example.com"
$env:DIGNA_API_TOKEN = "your-api-token"
```

Optional:

- `DIGNA_VERIFY_SSL` (`true`/`false`, defaults to `true`)
- `DIGNA_TIMEOUT_SECONDS` (numeric request timeout)

## Quick Start

```python
import os

from digna_sdk import DignaClient

api = DignaClient(
    base_url=os.environ["DIGNA_BASE_URL"],
    token=os.environ["DIGNA_API_TOKEN"],
)

projects = api.project.get_projects(limit=20)
print(f"Found {len(projects)} project(s)")
for project in projects:
    print(f"- {project.id}: {project.name}")
```

## Authentication and Client Options

You can construct `DignaClient` using:

- `base_url` + `token`
- an already configured `AuthenticatedClient`

Common options:

- `timeout`
- `verify_ssl`
- `follow_redirects`
- `headers` and `cookies`
- `raise_on_unexpected_status`

```python
import os

import httpx

from digna_sdk import DignaClient

api = DignaClient(
    base_url=os.environ["DIGNA_BASE_URL"],
    token=os.environ["DIGNA_API_TOKEN"],
    timeout=httpx.Timeout(30.0),
    verify_ssl=True,
    raise_on_unexpected_status=True,
)
```

## Error Handling

High-level methods raise:

- `NotFoundError` for missing resources
- `ApiResponseError` for documented API error payloads
- `UnexpectedStatus` for undocumented status codes when `raise_on_unexpected_status=True`

```python
from digna_sdk import ApiResponseError, DignaClient, NotFoundError

api = DignaClient("https://your-digna-instance.example.com", "token")

try:
    project = api.project.get_project(project_id=123)
    print(project.name)
except NotFoundError:
    print("Project not found")
except ApiResponseError as exc:
    print(f"Request failed: {exc}")
```

## Sync and Async Usage

Sync example:

```python
projects = api.project.get_projects(limit=50)
```

Async example:

```python
import asyncio
import os

from digna_sdk import DignaClient


async def main() -> None:
    api = DignaClient(
        base_url=os.environ["DIGNA_BASE_URL"],
        token=os.environ["DIGNA_API_TOKEN"],
    )
    projects = await api.project.get_projects_async(limit=50)
    print(f"Found {len(projects)} project(s)")


asyncio.run(main())
```

## Common Workflows

List data sources in a project:

```python
data_sources = api.data_source.get_data_sources(project_id=1, limit=100)
for data_source in data_sources:
    print(data_source.id, data_source.name)
```

List data sets for a data source:

```python
data_sets = api.data_set.get_data_sets(data_source_id=10, limit=100)
for data_set in data_sets:
    print(data_set.id, data_set.name)
```

Submit an inspection request:

```python
import datetime

from digna_sdk.models.stable_inspection_request_mode import StableInspectionRequestMode

api.inspection_request.submit_inspection_request(
    project_id=1,
    data_source_ids=[10, 11],
    include_all_data_sources=False,
    mode=StableInspectionRequestMode.WEEKLY,
    start_date=datetime.date(2026, 1, 1),
    end_date=datetime.date(2026, 1, 31),
    monthly_mode_days=[1],
    weekly_mode_weekdays=[1],
    use_notification=False,
)
```

## API Areas

- `attribute`
- `check_definition`
- `data_set`
- `data_source`
- `db_connection`
- `inspection_request`
- `inspection_status`
- `project`

Each area provides:

- `method`
- `method_detailed`
- `method_async`
- `method_async_detailed`

## Examples

Runnable examples live in `digna_sdk/examples` and use environment-based configuration.

- `digna_sdk/examples/list_projects.py`
- `digna_sdk/examples/list_data_sources.py`
- `digna_sdk/examples/list_data_sets.py`
- `digna_sdk/examples/submit_inspection_request.py`
- `digna_sdk/examples/async_list_projects.py`
- `digna_sdk/examples/error_handling.py`

See `digna_sdk/examples/README.md` for commands.

## Low-level Generated Endpoints

You can call generated endpoint modules directly if you prefer low-level control:

```python
from digna_sdk.api.project import get_project
from digna_sdk.client import AuthenticatedClient
from digna_sdk.models.api_error import ApiError
from digna_sdk.models.project import Project

client = AuthenticatedClient(base_url="https://api.example.com", token="<token>")
result: ApiError | Project | None = get_project.sync(project_id=1, client=client)
```

## Notes

- `DignaClient` is the recommended single entry point.
- `*_detailed` methods return `Response[...]` with status code and headers.
- Non-detailed methods return parsed success payloads and raise exceptions on API errors.
