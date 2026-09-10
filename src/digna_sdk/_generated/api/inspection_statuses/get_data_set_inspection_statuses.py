from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.dataset_inspection_status import DatasetInspectionStatus
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    data_source_id: int,
    dataset_id: int | Unset = UNSET,
    start_date: str,
    end_date: str,
    data_volume_status: int | Unset = UNSET,
    data_anomaly_status: int | Unset = UNSET,
    data_validation_status: int | Unset = UNSET,
    data_analytics_status: int | Unset = UNSET,
    inspection_status: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["data_source_id"] = data_source_id

    params["dataset_id"] = dataset_id

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["data_volume_status"] = data_volume_status

    params["data_anomaly_status"] = data_anomaly_status

    params["data_validation_status"] = data_validation_status

    params["data_analytics_status"] = data_analytics_status

    params["inspection_status"] = inspection_status

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/inspection-statuses/data-sets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | list[DatasetInspectionStatus] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DatasetInspectionStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | list[DatasetInspectionStatus]]:
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
    dataset_id: int | Unset = UNSET,
    start_date: str,
    end_date: str,
    data_volume_status: int | Unset = UNSET,
    data_anomaly_status: int | Unset = UNSET,
    data_validation_status: int | Unset = UNSET,
    data_analytics_status: int | Unset = UNSET,
    inspection_status: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiError | list[DatasetInspectionStatus]]:
    """
    Args:
        data_source_id (int):
        dataset_id (int | Unset):
        start_date (str):
        end_date (str):
        data_volume_status (int | Unset):
        data_anomaly_status (int | Unset):
        data_validation_status (int | Unset):
        data_analytics_status (int | Unset):
        inspection_status (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | list[DatasetInspectionStatus]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        dataset_id=dataset_id,
        start_date=start_date,
        end_date=end_date,
        data_volume_status=data_volume_status,
        data_anomaly_status=data_anomaly_status,
        data_validation_status=data_validation_status,
        data_analytics_status=data_analytics_status,
        inspection_status=inspection_status,
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
    dataset_id: int | Unset = UNSET,
    start_date: str,
    end_date: str,
    data_volume_status: int | Unset = UNSET,
    data_anomaly_status: int | Unset = UNSET,
    data_validation_status: int | Unset = UNSET,
    data_analytics_status: int | Unset = UNSET,
    inspection_status: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiError | list[DatasetInspectionStatus] | None:
    """
    Args:
        data_source_id (int):
        dataset_id (int | Unset):
        start_date (str):
        end_date (str):
        data_volume_status (int | Unset):
        data_anomaly_status (int | Unset):
        data_validation_status (int | Unset):
        data_analytics_status (int | Unset):
        inspection_status (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | list[DatasetInspectionStatus]
    """

    return sync_detailed(
        client=client,
        data_source_id=data_source_id,
        dataset_id=dataset_id,
        start_date=start_date,
        end_date=end_date,
        data_volume_status=data_volume_status,
        data_anomaly_status=data_anomaly_status,
        data_validation_status=data_validation_status,
        data_analytics_status=data_analytics_status,
        inspection_status=inspection_status,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    dataset_id: int | Unset = UNSET,
    start_date: str,
    end_date: str,
    data_volume_status: int | Unset = UNSET,
    data_anomaly_status: int | Unset = UNSET,
    data_validation_status: int | Unset = UNSET,
    data_analytics_status: int | Unset = UNSET,
    inspection_status: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiError | list[DatasetInspectionStatus]]:
    """
    Args:
        data_source_id (int):
        dataset_id (int | Unset):
        start_date (str):
        end_date (str):
        data_volume_status (int | Unset):
        data_anomaly_status (int | Unset):
        data_validation_status (int | Unset):
        data_analytics_status (int | Unset):
        inspection_status (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | list[DatasetInspectionStatus]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        dataset_id=dataset_id,
        start_date=start_date,
        end_date=end_date,
        data_volume_status=data_volume_status,
        data_anomaly_status=data_anomaly_status,
        data_validation_status=data_validation_status,
        data_analytics_status=data_analytics_status,
        inspection_status=inspection_status,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_source_id: int,
    dataset_id: int | Unset = UNSET,
    start_date: str,
    end_date: str,
    data_volume_status: int | Unset = UNSET,
    data_anomaly_status: int | Unset = UNSET,
    data_validation_status: int | Unset = UNSET,
    data_analytics_status: int | Unset = UNSET,
    inspection_status: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiError | list[DatasetInspectionStatus] | None:
    """
    Args:
        data_source_id (int):
        dataset_id (int | Unset):
        start_date (str):
        end_date (str):
        data_volume_status (int | Unset):
        data_anomaly_status (int | Unset):
        data_validation_status (int | Unset):
        data_analytics_status (int | Unset):
        inspection_status (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | list[DatasetInspectionStatus]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_id=data_source_id,
            dataset_id=dataset_id,
            start_date=start_date,
            end_date=end_date,
            data_volume_status=data_volume_status,
            data_anomaly_status=data_anomaly_status,
            data_validation_status=data_validation_status,
            data_analytics_status=data_analytics_status,
            inspection_status=inspection_status,
            limit=limit,
        )
    ).parsed
