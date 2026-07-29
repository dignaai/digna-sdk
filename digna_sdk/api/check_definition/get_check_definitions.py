from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.check_definition import CheckDefinition
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    data_source_id: int,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["data_source_id"] = data_source_id

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/check-definitions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | list[CheckDefinition] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = CheckDefinition.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | list[CheckDefinition]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    limit: int | Unset = UNSET,

) -> Response[ApiError | list[CheckDefinition]]:
    """get_check_definitions
    
    Tag: check_definition
    Operation: GET /v1/check-definitions
    
    Parameters:
        - data_source_id (query, required=True): Filter by data source ID
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: List check definitions
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        data_source_id=data_source_id,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    limit: int | Unset = UNSET,

) -> ApiError | list[CheckDefinition] | None:
    """get_check_definitions
    
    Tag: check_definition
    Operation: GET /v1/check-definitions
    
    Parameters:
        - data_source_id (query, required=True): Filter by data source ID
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: List check definitions
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        client=client,
data_source_id=data_source_id,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    limit: int | Unset = UNSET,

) -> Response[ApiError | list[CheckDefinition]]:
    """get_check_definitions
    
    Tag: check_definition
    Operation: GET /v1/check-definitions
    
    Parameters:
        - data_source_id (query, required=True): Filter by data source ID
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: List check definitions
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        data_source_id=data_source_id,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    limit: int | Unset = UNSET,

) -> ApiError | list[CheckDefinition] | None:
    """get_check_definitions
    
    Tag: check_definition
    Operation: GET /v1/check-definitions
    
    Parameters:
        - data_source_id (query, required=True): Filter by data source ID
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: List check definitions
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        client=client,
data_source_id=data_source_id,
limit=limit,

    )).parsed
