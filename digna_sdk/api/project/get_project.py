from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.project import Project
from typing import cast



def _get_kwargs(
    project_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}".format(project_id=quote(str(project_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | Project]:
    """get_project
    
    Tag: project
    Operation: GET /v1/projects/{project_id}
    
    Parameters:
        - project_id (path, required=True): Project ID
    
    Responses:
        - 200: Get a project
        - 404: Project not found
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | Project | None:
    """get_project
    
    Tag: project
    Operation: GET /v1/projects/{project_id}
    
    Parameters:
        - project_id (path, required=True): Project ID
    
    Responses:
        - 200: Get a project
        - 404: Project not found
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        project_id=project_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiError | Project]:
    """get_project
    
    Tag: project
    Operation: GET /v1/projects/{project_id}
    
    Parameters:
        - project_id (path, required=True): Project ID
    
    Responses:
        - 200: Get a project
        - 404: Project not found
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> ApiError | Project | None:
    """get_project
    
    Tag: project
    Operation: GET /v1/projects/{project_id}
    
    Parameters:
        - project_id (path, required=True): Project ID
    
    Responses:
        - 200: Get a project
        - 404: Project not found
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,

    )).parsed
