from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.inspection_request_status_response import InspectionRequestStatusResponse
from typing import cast



def _get_kwargs(
    inspection_request_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/inspection-requests/{inspection_request_id}".format(inspection_request_id=quote(str(inspection_request_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | InspectionRequestStatusResponse | None:
    if response.status_code == 200:
        response_200 = InspectionRequestStatusResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | InspectionRequestStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inspection_request_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | InspectionRequestStatusResponse]:
    """get_inspection_request
    
    Tag: inspection_request
    Operation: GET /v1/inspection-requests/{inspection_request_id}
    
    Parameters:
        - inspection_request_id (path, required=True): Inspection request ID
    
    Responses:
        - 200: Inspection request status
        - 401: Not authenticated
        - 403: Not authorized
        - 404: Inspection request not found
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        inspection_request_id=inspection_request_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    inspection_request_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | InspectionRequestStatusResponse | None:
    """get_inspection_request
    
    Tag: inspection_request
    Operation: GET /v1/inspection-requests/{inspection_request_id}
    
    Parameters:
        - inspection_request_id (path, required=True): Inspection request ID
    
    Responses:
        - 200: Inspection request status
        - 401: Not authenticated
        - 403: Not authorized
        - 404: Inspection request not found
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        inspection_request_id=inspection_request_id,
client=client,

    ).parsed

async def asyncio_detailed(
    inspection_request_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | InspectionRequestStatusResponse]:
    """get_inspection_request
    
    Tag: inspection_request
    Operation: GET /v1/inspection-requests/{inspection_request_id}
    
    Parameters:
        - inspection_request_id (path, required=True): Inspection request ID
    
    Responses:
        - 200: Inspection request status
        - 401: Not authenticated
        - 403: Not authorized
        - 404: Inspection request not found
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        inspection_request_id=inspection_request_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    inspection_request_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | InspectionRequestStatusResponse | None:
    """get_inspection_request
    
    Tag: inspection_request
    Operation: GET /v1/inspection-requests/{inspection_request_id}
    
    Parameters:
        - inspection_request_id (path, required=True): Inspection request ID
    
    Responses:
        - 200: Inspection request status
        - 401: Not authenticated
        - 403: Not authorized
        - 404: Inspection request not found
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        inspection_request_id=inspection_request_id,
client=client,

    )).parsed
