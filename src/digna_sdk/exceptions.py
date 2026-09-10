"""Exceptions raised by the Digna SDK."""

from __future__ import annotations

from ._generated.models.api_error_code import ApiErrorCode
from ._generated.models.stable_inspection_operation_status import StableInspectionOperationStatus


class DignaError(Exception):
    """Base class for all errors raised by the Digna SDK."""


class DignaConnectionError(DignaError):
    """Raised when the SDK could not reach the Digna backend."""


class DignaAPIError(DignaError):
    """Raised when the Digna API returns an error response.

    Attributes:
        status_code: The HTTP status code of the response.
        code: The machine-readable error code reported by the API, if any.
        message: The human-readable error message reported by the API.
    """

    def __init__(self, status_code: int, code: ApiErrorCode | None, message: str) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        super().__init__(f"[{status_code}] {code.value if code else 'UNKNOWN'}: {message}")


class DignaAuthenticationError(DignaAPIError):
    """Raised for 401 responses (missing/invalid credentials)."""


class DignaAuthorizationError(DignaAPIError):
    """Raised for 403 responses (authenticated but not permitted)."""


class DignaNotFoundError(DignaAPIError):
    """Raised for 404 responses."""


class DignaInspectionRequestFailed(DignaError):
    """Raised by `InspectionRequestsResource.wait_until_finished` when an inspection
    request reaches a non-successful terminal state (FAILED, ABORTED, or CANCELLED).
    """

    def __init__(self, inspection_request_id: int, status: StableInspectionOperationStatus) -> None:
        self.inspection_request_id = inspection_request_id
        self.status = status
        super().__init__(
            f"Inspection request {inspection_request_id} ended with status {status.value}"
        )
