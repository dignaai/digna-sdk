"""Internal httpx client that turns low-level HTTP failures into SDK exceptions."""

from __future__ import annotations

from typing import Any

import httpx

from ._convert import raise_api_error
from .exceptions import DignaConnectionError


class DignaHttpxClient(httpx.Client):
    """``httpx.Client`` whose failures surface as ``DignaError`` subclasses.

    The generated endpoint functions call ``httpx.Client.request`` directly and
    parse the body with ``response.json()``, so this is the single place where
    transport errors and non-JSON bodies can be intercepted for every endpoint.
    """

    def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        try:
            response = super().send(request, **kwargs)
        except httpx.TimeoutException as exc:
            raise DignaConnectionError(f"Request to {request.url} timed out: {exc}") from exc
        except httpx.TransportError as exc:
            raise DignaConnectionError(f"Could not reach {request.url}: {exc}") from exc
        if not kwargs.get("stream"):
            _ensure_json(response)
        return response


def _ensure_json(response: httpx.Response) -> None:
    """Raise ``DignaAPIError`` if a non-empty response body is not JSON.

    Every digna API response with a body is JSON; anything else (typically an
    HTML page served by a frontend or proxy) would otherwise crash the generated
    parser with a ``JSONDecodeError``.
    """
    content_type = response.headers.get("content-type", "")
    if not response.content or "json" in content_type:
        return
    if content_type.startswith("text/plain"):
        message = response.text
    else:
        message = (
            f"Expected a JSON response from {response.request.url} but got "
            f"'{content_type or 'no content type'}'. Check that base_url points at the "
            "digna API (it usually ends in '/api')."
        )
    raise_api_error(response.status_code, None, message)
