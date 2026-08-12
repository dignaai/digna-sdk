# digna_sdk examples

All examples use environment variables and optional CLI arguments.

## Required environment variables

- DIGNA_BASE_URL
- DIGNA_API_TOKEN

Optional:

- DIGNA_VERIFY_SSL (true/false, default true)
- DIGNA_TIMEOUT_SECONDS (number)

PowerShell setup:

```powershell
$env:DIGNA_BASE_URL = "https://your-digna-instance.example.com"
$env:DIGNA_API_TOKEN = "your-api-token"
$env:DIGNA_VERIFY_SSL = "true"
$env:DIGNA_TIMEOUT_SECONDS = "30"
```

## Commands

List projects:

```powershell
python -m digna_sdk.examples.list_projects --limit 20
```

List data sources for a project:

```powershell
python -m digna_sdk.examples.list_data_sources --project-id 1 --limit 50
```

List data sources and data set counts:

```powershell
python -m digna_sdk.examples.list_data_sources --project-id 1 --limit 50 --include-data-sets
```

List data sets for a data source:

```powershell
python -m digna_sdk.examples.list_data_sets --data-source-id 10 --limit 50
```

Submit a weekly inspection request:

```powershell
python -m digna_sdk.examples.submit_inspection_request --project-id 1 --data-source-id 10 --mode weekly --start-date 2026-01-01 --end-date 2026-01-31 --weekday 1
```

List projects asynchronously:

```powershell
python -m digna_sdk.examples.async_list_projects --limit 20
```

Error handling demonstration:

```powershell
python -m digna_sdk.examples.error_handling --project-id 123
```
