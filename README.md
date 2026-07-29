# digna_sdk
Official Python SDK for digna — the AI-driven Data Quality & Observability Platform.

Learn more about digna:

- https://www.digna.ai
- https://docs.digna.ai

## Quickstart

```python
from digna_sdk import DignaClient

api = DignaClient("https://api.example.com", "<token>")
project = api.project.get_project(project_id=1)
print(project.name)
```

## Error Handling
SDK wrapper methods return success types and raise exceptions for API errors.

```python
from digna_sdk import DignaClient
from digna_sdk import ApiResponseError, NotFoundError

api = DignaClient("https://api.example.com", "<token>")

try:
    project = api.project.get_project(project_id=999)
except NotFoundError:
    print("Project not found")
except ApiResponseError as exc:
    print(f"Call failed: {exc}")
```

## Slim Examples
- `examples/example.py`: minimal project fetch
- `examples/list_data_sources.py`: list data sources and data set counts
- `examples/submit_inspection_request.py`: flattened inspection-request submission

## API Surface
- `attribute` (AttributeApi): `create_attribute`, `delete_attribute`, `get_attribute`, `get_attributes`, `update_attribute`
- `check_definition` (CheckDefinitionApi): `get_check_definitions`
- `data_set` (DataSetApi): `create_data_set`, `delete_data_set`, `get_data_set`, `get_data_sets`, `update_data_set`
- `data_source` (DataSourceApi): `create_data_source`, `delete_data_source`, `get_data_source`, `get_data_sources`, `update_data_source`
- `db_connection` (DbConnectionApi): `get_db_connection`, `get_db_connections`
- `inspection_request` (InspectionRequestApi): `get_inspection_request`, `submit_inspection_request`
- `inspection_status` (InspectionStatusApi): `get_data_set_inspection_statuses`, `get_data_source_inspection_statuses`, `get_project_inspection_statuses`
- `project` (ProjectApi): `get_project`, `get_projects`

## Low-level endpoint modules
You can still call generated endpoint modules directly:

```python
from digna_sdk.api.project import get_project
from digna_sdk.client import AuthenticatedClient
from digna_sdk.models.project import Project
from digna_sdk.models.api_error import ApiError

client = AuthenticatedClient(base_url="https://api.example.com", token="<token>")
result: ApiError | Project | None = get_project.sync(project_id=1, client=client)
```

## Notes
- `DignaClient` is the recommended single entry point.
- `*_detailed` methods return `Response[...]` with status code and headers.
- Non-detailed methods return parsed success payloads and raise exceptions on API errors.
