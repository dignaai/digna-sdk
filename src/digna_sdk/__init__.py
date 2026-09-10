"""Digna Python SDK."""

from .client import DignaClient
from .exceptions import (
    DignaAPIError,
    DignaAuthenticationError,
    DignaAuthorizationError,
    DignaConnectionError,
    DignaError,
    DignaInspectionRequestFailed,
    DignaNotFoundError,
)

__version__ = "0.1.0"

__all__ = [
    "DignaClient",
    "DignaError",
    "DignaAPIError",
    "DignaAuthenticationError",
    "DignaAuthorizationError",
    "DignaNotFoundError",
    "DignaConnectionError",
    "DignaInspectionRequestFailed",
]
