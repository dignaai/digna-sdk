"""Internal helpers to convert generated (attrs) API objects into public pydantic models."""

from __future__ import annotations

from typing import TypeVar

from pydantic import BaseModel

from ._generated.models.api_error import ApiError
from ._generated.types import Response
from .exceptions import (
    DignaAPIError,
    DignaAuthenticationError,
    DignaAuthorizationError,
    DignaNotFoundError,
)

ModelT = TypeVar("ModelT", bound=BaseModel)


def unwrap(response: Response[object]) -> object:
    """Return the parsed body of a generated ``Response``, raising ``DignaAPIError`` on failure.

    A successful response with no body (e.g. ``204 No Content`` from a delete
    call) legitimately returns ``None``.
    """
    if response.status_code >= 300 or isinstance(response.parsed, ApiError):
        _raise_for_error(response)
    return response.parsed


def _raise_for_error(response: Response[object]) -> None:
    status_code = response.status_code
    if isinstance(response.parsed, ApiError):
        code = response.parsed.code
        message = response.parsed.message
    else:
        code = None
        message = response.content.decode("utf-8", errors="replace") or "Unknown error"

    if status_code == 401:
        raise DignaAuthenticationError(status_code, code, message)
    if status_code == 403:
        raise DignaAuthorizationError(status_code, code, message)
    if status_code == 404:
        raise DignaNotFoundError(status_code, code, message)
    raise DignaAPIError(status_code, code, message)


def to_model(model_cls: type[ModelT], attrs_obj: object) -> ModelT:
    """Convert a single generated attrs model instance into a pydantic model."""
    return model_cls.model_validate(attrs_obj.to_dict())  # type: ignore[attr-defined]


def to_model_list(model_cls: type[ModelT], attrs_objs: list[object]) -> list[ModelT]:
    """Convert a list of generated attrs model instances into pydantic models."""
    return [to_model(model_cls, obj) for obj in attrs_objs]
