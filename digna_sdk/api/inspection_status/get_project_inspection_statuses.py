from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.project_inspection_status import ProjectInspectionStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_id: int,
    start_date: str,
    end_date: str,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/inspection-statuses/projects",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | list[ProjectInspectionStatus] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProjectInspectionStatus.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | list[ProjectInspectionStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: int,
    start_date: str,
    end_date: str,
    limit: int | Unset = UNSET,

) -> Response[ApiError | list[ProjectInspectionStatus]]:
    """get_project_inspection_statuses
    
    Tag: inspection_status
    Operation: GET /v1/inspection-statuses/projects
    
    Parameters:
        - project_id (query, required=True): Project ID
        - start_date (query, required=True): Start date (YYYY-MM-DD)
        - end_date (query, required=True): End date (YYYY-MM-DD)
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: Get project inspection statuses
        - 500: Internal error
    
    Returns:
        Raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        project_id=project_id,
start_date=start_date,
end_date=end_date,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: int,
    start_date: str,
    end_date: str,
    limit: int | Unset = UNSET,

) -> ApiError | list[ProjectInspectionStatus] | None:
    """get_project_inspection_statuses
    
    Tag: inspection_status
    Operation: GET /v1/inspection-statuses/projects
    
    Parameters:
        - project_id (query, required=True): Project ID
        - start_date (query, required=True): Start date (YYYY-MM-DD)
        - end_date (query, required=True): End date (YYYY-MM-DD)
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: Get project inspection statuses
        - 500: Internal error
    
    Returns:
        Parsed response model for successful and handled error responses.
    """


    return sync_detailed(
        client=client,
project_id=project_id,
start_date=start_date,
end_date=end_date,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: int,
    start_date: str,
    end_date: str,
    limit: int | Unset = UNSET,

) -> Response[ApiError | list[ProjectInspectionStatus]]:
    """get_project_inspection_statuses
    
    Tag: inspection_status
    Operation: GET /v1/inspection-statuses/projects
    
    Parameters:
        - project_id (query, required=True): Project ID
        - start_date (query, required=True): Start date (YYYY-MM-DD)
        - end_date (query, required=True): End date (YYYY-MM-DD)
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: Get project inspection statuses
        - 500: Internal error
    
    Returns:
        Async raw response wrapper with parsed payload.
    """


    kwargs = _get_kwargs(
        project_id=project_id,
start_date=start_date,
end_date=end_date,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: int,
    start_date: str,
    end_date: str,
    limit: int | Unset = UNSET,

) -> ApiError | list[ProjectInspectionStatus] | None:
    """get_project_inspection_statuses
    
    Tag: inspection_status
    Operation: GET /v1/inspection-statuses/projects
    
    Parameters:
        - project_id (query, required=True): Project ID
        - start_date (query, required=True): Start date (YYYY-MM-DD)
        - end_date (query, required=True): End date (YYYY-MM-DD)
        - limit (query, required=False): Maximum number of rows to return (default: 200, max: 5000)
    
    Responses:
        - 200: Get project inspection statuses
        - 500: Internal error
    
    Returns:
        Async parsed response model for successful and handled error responses.
    """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
start_date=start_date,
end_date=end_date,
limit=limit,

    )).parsed
