from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.db_connection import DbConnection
from typing import cast



def _get_kwargs(
    db_connection_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/db-connections/{db_connection_id}".format(db_connection_id=quote(str(db_connection_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | DbConnection | None:
    if response.status_code == 200:
        response_200 = DbConnection.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | DbConnection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    db_connection_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | DbConnection]:
    """get_db_connection
    
    Tag: db_connection
    Operation: GET /v1/db-connections/{db_connection_id}
    
    Parameters:
        - db_connection_id (path, required=True): Db connection ID
    
    Responses:
        - 200: Get a db connection
        - 404: Db connection not found
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        db_connection_id=db_connection_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    db_connection_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | DbConnection | None:
    """get_db_connection
    
    Tag: db_connection
    Operation: GET /v1/db-connections/{db_connection_id}
    
    Parameters:
        - db_connection_id (path, required=True): Db connection ID
    
    Responses:
        - 200: Get a db connection
        - 404: Db connection not found
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        db_connection_id=db_connection_id,
client=client,

    ).parsed

async def asyncio_detailed(
    db_connection_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | DbConnection]:
    """get_db_connection
    
    Tag: db_connection
    Operation: GET /v1/db-connections/{db_connection_id}
    
    Parameters:
        - db_connection_id (path, required=True): Db connection ID
    
    Responses:
        - 200: Get a db connection
        - 404: Db connection not found
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        db_connection_id=db_connection_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    db_connection_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | DbConnection | None:
    """get_db_connection
    
    Tag: db_connection
    Operation: GET /v1/db-connections/{db_connection_id}
    
    Parameters:
        - db_connection_id (path, required=True): Db connection ID
    
    Responses:
        - 200: Get a db connection
        - 404: Db connection not found
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        db_connection_id=db_connection_id,
client=client,

    )).parsed
