from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from typing import cast



def _get_kwargs(
    attribute_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/attributes/{attribute_id}".format(attribute_id=quote(str(attribute_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ApiError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiError]:
    """delete_attribute
    
    Tag: attribute
    Operation: DELETE /v1/attributes/{attribute_id}
    
    Parameters:
        - attribute_id (path, required=True): Attribute ID
    
    Responses:
        - 204: Delete an attribute
        - 404: Attribute not found
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        attribute_id=attribute_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    attribute_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiError | None:
    """delete_attribute
    
    Tag: attribute
    Operation: DELETE /v1/attributes/{attribute_id}
    
    Parameters:
        - attribute_id (path, required=True): Attribute ID
    
    Responses:
        - 204: Delete an attribute
        - 404: Attribute not found
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        attribute_id=attribute_id,
client=client,

    ).parsed

async def asyncio_detailed(
    attribute_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiError]:
    """delete_attribute
    
    Tag: attribute
    Operation: DELETE /v1/attributes/{attribute_id}
    
    Parameters:
        - attribute_id (path, required=True): Attribute ID
    
    Responses:
        - 204: Delete an attribute
        - 404: Attribute not found
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        attribute_id=attribute_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    attribute_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiError | None:
    """delete_attribute
    
    Tag: attribute
    Operation: DELETE /v1/attributes/{attribute_id}
    
    Parameters:
        - attribute_id (path, required=True): Attribute ID
    
    Responses:
        - 204: Delete an attribute
        - 404: Attribute not found
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        attribute_id=attribute_id,
client=client,

    )).parsed
