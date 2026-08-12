import os

import httpx

from digna_sdk import DignaClient


BASE_URL_ENV = "DIGNA_BASE_URL"
TOKEN_ENV = "DIGNA_API_TOKEN"
VERIFY_SSL_ENV = "DIGNA_VERIFY_SSL"
TIMEOUT_SECONDS_ENV = "DIGNA_TIMEOUT_SECONDS"


class ExampleConfigurationError(RuntimeError):
    """Raised when required example configuration is missing or invalid."""


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise ExampleConfigurationError(
            f"Missing required environment variable {name}. "
            f"Set it before running examples."
        )
    return value


def _parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    raise ExampleConfigurationError(
        f"Invalid boolean value '{value}' for {VERIFY_SSL_ENV}. "
        "Use true/false."
    )


def get_client() -> DignaClient:
    """Build a DignaClient from environment variables used by all examples."""
    base_url = _require_env(BASE_URL_ENV)
    token = _require_env(TOKEN_ENV)

    verify_ssl_raw = os.getenv(VERIFY_SSL_ENV, "true")
    verify_ssl = _parse_bool(verify_ssl_raw)

    timeout_raw = os.getenv(TIMEOUT_SECONDS_ENV)
    if timeout_raw is None or timeout_raw.strip() == "":
        timeout = None
    else:
        try:
            timeout = httpx.Timeout(float(timeout_raw))
        except ValueError as exc:
            raise ExampleConfigurationError(
                f"Invalid numeric timeout '{timeout_raw}' for {TIMEOUT_SECONDS_ENV}."
            ) from exc

    return DignaClient(
        base_url=base_url,
        token=token,
        verify_ssl=verify_ssl,
        timeout=timeout,
    )
