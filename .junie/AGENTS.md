# Project Overview — digna-python-sdk

This file stores a high-level overview of the project for future reference.

## What this is

The **official Python SDK for [Digna](https://digna.ai)**, a data-quality and observability platform. It's a client library (published as `digna-sdk`) that lets Python code talk to the Digna REST API in a clean, typed, "pythonic" way instead of hand-crafting HTTP requests.

## Purpose

Digna inspects datasets for data-quality issues. This SDK wraps its stable `/v1` HTTP API so you can manage projects, data sources/sets, attributes, checks, DB connections, and trigger/monitor **inspection runs** from Python.

## Architecture (two layers)

The codebase is deliberately split into a machine-generated layer and a hand-written friendly layer:

1. **Generated layer** — `src/digna_sdk/_generated/`
   - Auto-generated from the OpenAPI spec at `spec/openapi.json` using `openapi-python-client`.
   - Contains the low-level `AuthenticatedClient`, one module per endpoint under `api/` (e.g. `projects/get_projects.py`), and `attrs`-based `models/`.
   - Treated as throwaway/regenerable code — `pyproject.toml` excludes it from linting (`"src/digna_sdk/_generated/**" = ["ALL"]`).

2. **Hand-written pythonic layer** — the rest of `src/digna_sdk/`
   - `client.py` — main entry point `DignaClient(base_url, token)`. Constructs the underlying authenticated HTTP client and exposes namespaced resources: `client.projects`, `client.data_sources`, `client.data_sets`, `client.attributes`, `client.check_definitions`, `client.db_connections`, `client.inspection_requests`, `client.inspection_statuses`. It's also a context manager and manages the connection pool.
   - `resources/` — one small facade class per resource with methods like `.list()` / `.get()` / `.submit()` that call the generated endpoints and return clean models. The most interesting one, `inspection_requests.py`, adds `submit(...)`, `get_status(...)`, and a convenience `wait_until_finished(...)` that **polls** until an inspection reaches a terminal state (COMPLETED/FAILED/ABORTED/CANCELLED), raising on failure or timeout.
   - `models.py` — the public, clean data models returned to users.
   - `_convert.py` — helpers (`unwrap`, `to_model`, `to_model_list`) that turn generated responses into the public models and surface API errors.
   - `exceptions.py` — user-facing exception hierarchy: `DignaError` → `DignaAPIError`, `DignaAuthenticationError`, `DignaAuthorizationError`, `DignaNotFoundError`, `DignaConnectionError`, `DignaInspectionRequestFailed`.

## Usage example

```python
from digna_sdk import DignaClient

client = DignaClient(base_url="http://localhost:8000", token="<your-api-token>")
for project in client.projects.list():
    print(project.id, project.name)
```

## Supporting pieces

- `spec/openapi.json` — the source of truth from which the generated layer is produced.
- `tests/` — `pytest` suite using `respx` to mock httpx calls (`test_projects.py`, `test_data_sources.py`, `test_inspections.py`, `test_inspection_requests_wait.py`), with fixtures in `conftest.py`.
- `examples/` — runnable samples (`quickstart.py`, `inspection_flow.py`).
- `docs/` + `mkdocs.yml` + `site/` — MkDocs (Material theme, `mkdocstrings`) documentation, published at docs.digna.ai.
- `pyproject.toml` — Hatchling build, requires Python >= 3.10, runtime deps `httpx`, `attrs`, `python-dateutil`, `pydantic`; dev tooling includes `pytest`, `ruff`, `mypy`, and `openapi-python-client`.

## Mental model

**OpenAPI spec → generated raw client (`_generated`) → thin pythonic wrappers (`resources` + `models` + `client`) → what users import.** You interact only with `DignaClient` and its resource namespaces; the generated code stays hidden behind `_` prefixes and can be regenerated whenever the API spec changes.
