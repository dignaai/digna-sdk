# Digna Python SDK

Official Python SDK for **Digna**, the on-premises data-quality and observability
platform. It wraps a stable, versioned REST API with a small, pythonic,
[pydantic](https://docs.pydantic.dev/)-typed client.

## Why this SDK?

- **Typed models** — every request and response is validated with pydantic, so
  your editor and type checker catch mistakes before you hit the network.
- **Resource-oriented** — `client.projects`, `client.data_sources`,
  `client.data_sets`, `client.attributes`, `client.check_definitions`,
  `client.db_connections`, `client.inspection_requests`, and
  `client.inspection_statuses` each expose simple `list` / `get` / `create` /
  `update` / `delete` methods.
- **Clear errors** — API errors raise `DignaAPIError` (or a more specific
  subclass like `DignaAuthenticationError`, `DignaAuthorizationError`, or
  `DignaNotFoundError`) instead of silently returning `None`.

## Installation

```bash
pip install digna-sdk
```

## Next steps

- [Quickstart](quickstart.md) — connect and make your first calls.
- [Resources](resources.md) — the full list of available resource clients.
- [Models](models.md) — the pydantic models used for input/output.
- [Errors](errors.md) — the exception hierarchy.
- [API Reference](reference.md) — auto-generated reference docs.
