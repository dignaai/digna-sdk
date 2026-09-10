# Digna Python SDK

Official Python SDK for [Digna](https://digna.ai), the data-quality and observability platform.

## Installation

```bash
pip install digna-sdk
```

## Quickstart

```python
from digna_sdk import DignaClient

client = DignaClient(base_url="http://localhost:8000", token="<your-api-token>")

projects = client.projects.list()
for project in projects:
    print(project.id, project.name)
```

## Development

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
uv pip install -e ".[dev,docs]"
pytest
```

See [docs/](https://docs.digna.ai/) for full documentation.
