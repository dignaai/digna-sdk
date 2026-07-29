from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.create_data_set_request import CreateDataSetRequest
from ...models.data_set import DataSet
from typing import cast



def _get_kwargs(
    *,
    body: CreateDataSetRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/data-sets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | DataSet | None:
    if response.status_code == 201:
        response_201 = DataSet.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | DataSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataSetRequest,

) -> Response[ApiError | DataSet]:
    """create_data_set
    
    Tag: data_set
    Operation: POST /v1/data-sets
    
    Responses:
        - 201: Create a data set
        - 404: Not found
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataSetRequest,

) -> ApiError | DataSet | None:
    """create_data_set
    
    Tag: data_set
    Operation: POST /v1/data-sets
    
    Responses:
        - 201: Create a data set
        - 404: Not found
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataSetRequest,

) -> Response[ApiError | DataSet]:
    """create_data_set
    
    Tag: data_set
    Operation: POST /v1/data-sets
    
    Responses:
        - 201: Create a data set
        - 404: Not found
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataSetRequest,

) -> ApiError | DataSet | None:
    """create_data_set
    
    Tag: data_set
    Operation: POST /v1/data-sets
    
    Responses:
        - 201: Create a data set
        - 404: Not found
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
