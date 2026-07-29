"""Area-based facade over generated Digna SDK endpoint functions."""

from __future__ import annotations

from .client import AuthenticatedClient
from .api.attribute import create_attribute as attribute_create_attribute
from .api.attribute import delete_attribute as attribute_delete_attribute
from .api.attribute import get_attribute as attribute_get_attribute
from .api.attribute import get_attributes as attribute_get_attributes
from .api.attribute import update_attribute as attribute_update_attribute
from .api.check_definition import get_check_definitions as check_definition_get_check_definitions
from .api.data_set import create_data_set as data_set_create_data_set
from .api.data_set import delete_data_set as data_set_delete_data_set
from .api.data_set import get_data_set as data_set_get_data_set
from .api.data_set import get_data_sets as data_set_get_data_sets
from .api.data_set import update_data_set as data_set_update_data_set
from .api.data_source import create_data_source as data_source_create_data_source
from .api.data_source import delete_data_source as data_source_delete_data_source
from .api.data_source import get_data_source as data_source_get_data_source
from .api.data_source import get_data_sources as data_source_get_data_sources
from .api.data_source import update_data_source as data_source_update_data_source
from .api.db_connection import get_db_connection as db_connection_get_db_connection
from .api.db_connection import get_db_connections as db_connection_get_db_connections
from .api.inspection_request import get_inspection_request as inspection_request_get_inspection_request
from .api.inspection_request import submit_inspection_request as inspection_request_submit_inspection_request
from .api.inspection_status import get_data_set_inspection_statuses as inspection_status_get_data_set_inspection_statuses
from .api.inspection_status import get_data_source_inspection_statuses as inspection_status_get_data_source_inspection_statuses
from .api.inspection_status import get_project_inspection_statuses as inspection_status_get_project_inspection_statuses
from .api.project import get_project as project_get_project
from .api.project import get_projects as project_get_projects
from .models.api_error import ApiError
from .models.attribute import Attribute
from .models.check_definition import CheckDefinition
from .models.create_attribute_request import CreateAttributeRequest
from .models.create_data_set_request import CreateDataSetRequest
from .models.create_data_source_request import CreateDataSourceRequest
from .models.create_project_request import CreateProjectRequest
from .models.data_set import DataSet
from .models.data_source import DataSource
from .models.data_source_inspection_status import DataSourceInspectionStatus
from .models.data_source_modules import DataSourceModules
from .models.data_source_object import DataSourceObject
from .models.dataset_inspection_status import DatasetInspectionStatus
from .models.db_connection import DbConnection
from .models.inspection_request_status_response import InspectionRequestStatusResponse
from .models.project import Project
from .models.project_inspection_status import ProjectInspectionStatus
from .models.stable_attribute_category import StableAttributeCategory
from .models.stable_data_set_kind import StableDataSetKind
from .models.stable_data_source_kind import StableDataSourceKind
from .models.stable_inspection_request_mode import StableInspectionRequestMode
from .models.submit_inspection_request import SubmitInspectionRequest
from .models.update_attribute_request import UpdateAttributeRequest
from .models.update_data_set_request import UpdateDataSetRequest
from .models.update_data_source_request import UpdateDataSourceRequest
from .models.update_project_request import UpdateProjectRequest
from .types import Response
from .types import UNSET
from .types import Unset
from typing import Any
import datetime

class ApiResponseError(Exception):
    """Raised when an endpoint returns a documented API error payload."""

    def __init__(self, operation: str, status_code: int, error: ApiError | None = None) -> None:
        self.operation = operation
        self.status_code = status_code
        self.error = error
        if error is None:
            message = f"{operation} failed with status {status_code}"
        else:
            message = f"{operation} failed with status {status_code}: {error.code} - {error.message}"
        super().__init__(message)


class NotFoundError(ApiResponseError):
    """Raised when an endpoint returns 404 or no payload where payload is expected."""

    def __init__(self, operation: str, error: ApiError | None = None) -> None:
        super().__init__(operation=operation, status_code=404, error=error)


def _expect_success(
    *,
    operation: str,
    response: Response[Any],
    success_statuses: set[int],
    allow_none: bool,
) -> Any:
    status_code = int(response.status_code)
    parsed = response.parsed

    if status_code not in success_statuses:
        if status_code == 404:
            raise NotFoundError(operation=operation, error=parsed if isinstance(parsed, ApiError) else None)
        raise ApiResponseError(operation=operation, status_code=status_code, error=parsed if isinstance(parsed, ApiError) else None)

    if isinstance(parsed, ApiError):
        if status_code == 404:
            raise NotFoundError(operation=operation, error=parsed)
        raise ApiResponseError(operation=operation, status_code=status_code, error=parsed)

    if parsed is None and not allow_none:
        raise NotFoundError(operation=operation)

    return parsed


class AttributeApi:
    """Attribute endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def create_attribute_detailed(self, *, category: StableAttributeCategory, data_source_id: int, data_type: str, name: str, statistic_ids: list[int]) -> Response[Attribute]:
        """Create Attribute
        
        Flattened convenience method that builds CreateAttributeRequest internally.
        """
        body = CreateAttributeRequest(
            category=category,
            data_source_id=data_source_id,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = attribute_create_attribute.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_attribute", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def create_attribute(self, *, category: StableAttributeCategory, data_source_id: int, data_type: str, name: str, statistic_ids: list[int]) -> Attribute:
        """Create Attribute
        
        Flattened convenience method that builds CreateAttributeRequest internally.
        """
        body = CreateAttributeRequest(
            category=category,
            data_source_id=data_source_id,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = attribute_create_attribute.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="create_attribute", response=response, success_statuses={201}, allow_none=False)

    async def create_attribute_async(self, *, category: StableAttributeCategory, data_source_id: int, data_type: str, name: str, statistic_ids: list[int]) -> Attribute:
        """Create Attribute
        
        Flattened convenience method that builds CreateAttributeRequest internally.
        """
        body = CreateAttributeRequest(
            category=category,
            data_source_id=data_source_id,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = await attribute_create_attribute.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="create_attribute", response=response, success_statuses={201}, allow_none=False)

    async def create_attribute_async_detailed(self, *, category: StableAttributeCategory, data_source_id: int, data_type: str, name: str, statistic_ids: list[int]) -> Response[Attribute]:
        """Create Attribute
        
        Flattened convenience method that builds CreateAttributeRequest internally.
        """
        body = CreateAttributeRequest(
            category=category,
            data_source_id=data_source_id,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = await attribute_create_attribute.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_attribute", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_attribute_detailed(self, attribute_id: int) -> Response[None]:
        """Delete Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Response[None]: Delete an attribute. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_delete_attribute.sync_detailed(attribute_id=attribute_id, client=self._client)
        parsed = _expect_success(operation="delete_attribute", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_attribute(self, attribute_id: int) -> None:
        """Delete Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            None: Delete an attribute
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_delete_attribute.sync_detailed(attribute_id=attribute_id, client=self._client)
        return _expect_success(operation="delete_attribute", response=response, success_statuses={204}, allow_none=True)

    async def delete_attribute_async(self, attribute_id: int) -> None:
        """Delete Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            None: Delete an attribute
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_delete_attribute.asyncio_detailed(attribute_id=attribute_id, client=self._client)
        return _expect_success(operation="delete_attribute", response=response, success_statuses={204}, allow_none=True)

    async def delete_attribute_async_detailed(self, attribute_id: int) -> Response[None]:
        """Delete Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Response[None]: Delete an attribute. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_delete_attribute.asyncio_detailed(attribute_id=attribute_id, client=self._client)
        parsed = _expect_success(operation="delete_attribute", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_attribute_detailed(self, attribute_id: int) -> Response[Attribute]:
        """Get Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Response[Attribute]: Get an attribute. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_get_attribute.sync_detailed(attribute_id=attribute_id, client=self._client)
        parsed = _expect_success(operation="get_attribute", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_attribute(self, attribute_id: int) -> Attribute:
        """Get Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Attribute: Get an attribute
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_get_attribute.sync_detailed(attribute_id=attribute_id, client=self._client)
        return _expect_success(operation="get_attribute", response=response, success_statuses={200}, allow_none=False)

    async def get_attribute_async(self, attribute_id: int) -> Attribute:
        """Get Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Attribute: Get an attribute
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_get_attribute.asyncio_detailed(attribute_id=attribute_id, client=self._client)
        return _expect_success(operation="get_attribute", response=response, success_statuses={200}, allow_none=False)

    async def get_attribute_async_detailed(self, attribute_id: int) -> Response[Attribute]:
        """Get Attribute
        
        Args:
            attribute_id (int, required): Attribute ID
        
        Returns:
            Response[Attribute]: Get an attribute. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_get_attribute.asyncio_detailed(attribute_id=attribute_id, client=self._client)
        parsed = _expect_success(operation="get_attribute", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_attributes_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[Attribute]]:
        """Get Attributes
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[Attribute]]: List attributes. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_get_attributes.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_attributes", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_attributes(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[Attribute]:
        """Get Attributes
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[Attribute]: List attributes
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = attribute_get_attributes.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_attributes", response=response, success_statuses={200}, allow_none=False)

    async def get_attributes_async(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[Attribute]:
        """Get Attributes
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[Attribute]: List attributes
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_get_attributes.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_attributes", response=response, success_statuses={200}, allow_none=False)

    async def get_attributes_async_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[Attribute]]:
        """Get Attributes
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[Attribute]]: List attributes. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await attribute_get_attributes.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_attributes", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_attribute_detailed(self, attribute_id: int, *, category: StableAttributeCategory, data_type: str, name: str, statistic_ids: list[int]) -> Response[Attribute]:
        """Update Attribute
        
        Flattened convenience method that builds UpdateAttributeRequest internally.
        """
        body = UpdateAttributeRequest(
            category=category,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = attribute_update_attribute.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_attribute", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_attribute(self, attribute_id: int, *, category: StableAttributeCategory, data_type: str, name: str, statistic_ids: list[int]) -> Attribute:
        """Update Attribute
        
        Flattened convenience method that builds UpdateAttributeRequest internally.
        """
        body = UpdateAttributeRequest(
            category=category,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = attribute_update_attribute.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="update_attribute", response=response, success_statuses={200}, allow_none=False)

    async def update_attribute_async(self, attribute_id: int, *, category: StableAttributeCategory, data_type: str, name: str, statistic_ids: list[int]) -> Attribute:
        """Update Attribute
        
        Flattened convenience method that builds UpdateAttributeRequest internally.
        """
        body = UpdateAttributeRequest(
            category=category,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = await attribute_update_attribute.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="update_attribute", response=response, success_statuses={200}, allow_none=False)

    async def update_attribute_async_detailed(self, attribute_id: int, *, category: StableAttributeCategory, data_type: str, name: str, statistic_ids: list[int]) -> Response[Attribute]:
        """Update Attribute
        
        Flattened convenience method that builds UpdateAttributeRequest internally.
        """
        body = UpdateAttributeRequest(
            category=category,
            data_type=data_type,
            name=name,
            statistic_ids=statistic_ids,
        )
        response = await attribute_update_attribute.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_attribute", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class CheckDefinitionApi:
    """Check definition endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get_check_definitions_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[CheckDefinition]]:
        """Get Check Definitions
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[CheckDefinition]]: List check definitions. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = check_definition_get_check_definitions.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_check_definitions", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_check_definitions(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[CheckDefinition]:
        """Get Check Definitions
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[CheckDefinition]: List check definitions
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = check_definition_get_check_definitions.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_check_definitions", response=response, success_statuses={200}, allow_none=False)

    async def get_check_definitions_async(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[CheckDefinition]:
        """Get Check Definitions
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[CheckDefinition]: List check definitions
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await check_definition_get_check_definitions.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_check_definitions", response=response, success_statuses={200}, allow_none=False)

    async def get_check_definitions_async_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[CheckDefinition]]:
        """Get Check Definitions
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[CheckDefinition]]: List check definitions. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await check_definition_get_check_definitions.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_check_definitions", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class DataSetApi:
    """Data set endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def create_data_set_detailed(self, *, data_source_id: int, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> Response[DataSet]:
        """Create Data Set
        
        Flattened convenience method that builds CreateDataSetRequest internally.
        """
        body = CreateDataSetRequest(
            data_source_id=data_source_id,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = data_set_create_data_set.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_data_set", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def create_data_set(self, *, data_source_id: int, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> DataSet:
        """Create Data Set
        
        Flattened convenience method that builds CreateDataSetRequest internally.
        """
        body = CreateDataSetRequest(
            data_source_id=data_source_id,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = data_set_create_data_set.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="create_data_set", response=response, success_statuses={201}, allow_none=False)

    async def create_data_set_async(self, *, data_source_id: int, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> DataSet:
        """Create Data Set
        
        Flattened convenience method that builds CreateDataSetRequest internally.
        """
        body = CreateDataSetRequest(
            data_source_id=data_source_id,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = await data_set_create_data_set.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="create_data_set", response=response, success_statuses={201}, allow_none=False)

    async def create_data_set_async_detailed(self, *, data_source_id: int, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> Response[DataSet]:
        """Create Data Set
        
        Flattened convenience method that builds CreateDataSetRequest internally.
        """
        body = CreateDataSetRequest(
            data_source_id=data_source_id,
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = await data_set_create_data_set.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_data_set", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_data_set_detailed(self, dataset_id: int) -> Response[None]:
        """Delete Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            Response[None]: Delete a data set. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_delete_data_set.sync_detailed(dataset_id=dataset_id, client=self._client)
        parsed = _expect_success(operation="delete_data_set", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_data_set(self, dataset_id: int) -> None:
        """Delete Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            None: Delete a data set
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_delete_data_set.sync_detailed(dataset_id=dataset_id, client=self._client)
        return _expect_success(operation="delete_data_set", response=response, success_statuses={204}, allow_none=True)

    async def delete_data_set_async(self, dataset_id: int) -> None:
        """Delete Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            None: Delete a data set
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_delete_data_set.asyncio_detailed(dataset_id=dataset_id, client=self._client)
        return _expect_success(operation="delete_data_set", response=response, success_statuses={204}, allow_none=True)

    async def delete_data_set_async_detailed(self, dataset_id: int) -> Response[None]:
        """Delete Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            Response[None]: Delete a data set. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_delete_data_set.asyncio_detailed(dataset_id=dataset_id, client=self._client)
        parsed = _expect_success(operation="delete_data_set", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_set_detailed(self, dataset_id: int) -> Response[DataSet]:
        """Get Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            Response[DataSet]: Get a data set. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_get_data_set.sync_detailed(dataset_id=dataset_id, client=self._client)
        parsed = _expect_success(operation="get_data_set", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_set(self, dataset_id: int) -> DataSet:
        """Get Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            DataSet: Get a data set
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_get_data_set.sync_detailed(dataset_id=dataset_id, client=self._client)
        return _expect_success(operation="get_data_set", response=response, success_statuses={200}, allow_none=False)

    async def get_data_set_async(self, dataset_id: int) -> DataSet:
        """Get Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            DataSet: Get a data set
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_get_data_set.asyncio_detailed(dataset_id=dataset_id, client=self._client)
        return _expect_success(operation="get_data_set", response=response, success_statuses={200}, allow_none=False)

    async def get_data_set_async_detailed(self, dataset_id: int) -> Response[DataSet]:
        """Get Data Set
        
        Args:
            dataset_id (int, required): Data set ID
        
        Returns:
            Response[DataSet]: Get a data set. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_get_data_set.asyncio_detailed(dataset_id=dataset_id, client=self._client)
        parsed = _expect_success(operation="get_data_set", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_sets_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[DataSet]]:
        """Get Data Sets
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSet]]: List data sets. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_get_data_sets.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_sets", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_sets(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[DataSet]:
        """Get Data Sets
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSet]: List data sets
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_set_get_data_sets.sync_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_data_sets", response=response, success_statuses={200}, allow_none=False)

    async def get_data_sets_async(self, *, data_source_id: int, limit: int | Unset = UNSET) -> list[DataSet]:
        """Get Data Sets
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSet]: List data sets
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_get_data_sets.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        return _expect_success(operation="get_data_sets", response=response, success_statuses={200}, allow_none=False)

    async def get_data_sets_async_detailed(self, *, data_source_id: int, limit: int | Unset = UNSET) -> Response[list[DataSet]]:
        """Get Data Sets
        
        Args:
            data_source_id (int, required): Filter by data source ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSet]]: List data sets. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_set_get_data_sets.asyncio_detailed(data_source_id=data_source_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_sets", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_data_set_detailed(self, dataset_id: int, *, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> Response[DataSet]:
        """Update Data Set
        
        Flattened convenience method that builds UpdateDataSetRequest internally.
        """
        body = UpdateDataSetRequest(
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = data_set_update_data_set.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_data_set", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_data_set(self, dataset_id: int, *, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> DataSet:
        """Update Data Set
        
        Flattened convenience method that builds UpdateDataSetRequest internally.
        """
        body = UpdateDataSetRequest(
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = data_set_update_data_set.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="update_data_set", response=response, success_statuses={200}, allow_none=False)

    async def update_data_set_async(self, dataset_id: int, *, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> DataSet:
        """Update Data Set
        
        Flattened convenience method that builds UpdateDataSetRequest internally.
        """
        body = UpdateDataSetRequest(
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = await data_set_update_data_set.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="update_data_set", response=response, success_statuses={200}, allow_none=False)

    async def update_data_set_async_detailed(self, dataset_id: int, *, filter_expression: str, grouping_expression: str, kind: StableDataSetKind, name: str) -> Response[DataSet]:
        """Update Data Set
        
        Flattened convenience method that builds UpdateDataSetRequest internally.
        """
        body = UpdateDataSetRequest(
            filter_expression=filter_expression,
            grouping_expression=grouping_expression,
            kind=kind,
            name=name,
        )
        response = await data_set_update_data_set.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_data_set", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class DataSourceApi:
    """Data source endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def create_data_source_detailed(self, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, project_id: int, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> Response[DataSource]:
        """Create Data Source
        
        Flattened convenience method that builds CreateDataSourceRequest internally.
        """
        body = CreateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            project_id=project_id,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = data_source_create_data_source.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_data_source", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def create_data_source(self, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, project_id: int, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> DataSource:
        """Create Data Source
        
        Flattened convenience method that builds CreateDataSourceRequest internally.
        """
        body = CreateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            project_id=project_id,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = data_source_create_data_source.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="create_data_source", response=response, success_statuses={201}, allow_none=False)

    async def create_data_source_async(self, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, project_id: int, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> DataSource:
        """Create Data Source
        
        Flattened convenience method that builds CreateDataSourceRequest internally.
        """
        body = CreateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            project_id=project_id,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = await data_source_create_data_source.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="create_data_source", response=response, success_statuses={201}, allow_none=False)

    async def create_data_source_async_detailed(self, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, project_id: int, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> Response[DataSource]:
        """Create Data Source
        
        Flattened convenience method that builds CreateDataSourceRequest internally.
        """
        body = CreateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            project_id=project_id,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = await data_source_create_data_source.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="create_data_source", response=response, success_statuses={201}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_data_source_detailed(self, data_source_id: int) -> Response[None]:
        """Delete Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            Response[None]: Delete a data source. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_delete_data_source.sync_detailed(data_source_id=data_source_id, client=self._client)
        parsed = _expect_success(operation="delete_data_source", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def delete_data_source(self, data_source_id: int) -> None:
        """Delete Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            None: Delete a data source
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_delete_data_source.sync_detailed(data_source_id=data_source_id, client=self._client)
        return _expect_success(operation="delete_data_source", response=response, success_statuses={204}, allow_none=True)

    async def delete_data_source_async(self, data_source_id: int) -> None:
        """Delete Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            None: Delete a data source
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_delete_data_source.asyncio_detailed(data_source_id=data_source_id, client=self._client)
        return _expect_success(operation="delete_data_source", response=response, success_statuses={204}, allow_none=True)

    async def delete_data_source_async_detailed(self, data_source_id: int) -> Response[None]:
        """Delete Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            Response[None]: Delete a data source. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_delete_data_source.asyncio_detailed(data_source_id=data_source_id, client=self._client)
        parsed = _expect_success(operation="delete_data_source", response=response, success_statuses={204}, allow_none=True)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_source_detailed(self, data_source_id: int) -> Response[DataSource]:
        """Get Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            Response[DataSource]: Get a data source. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_get_data_source.sync_detailed(data_source_id=data_source_id, client=self._client)
        parsed = _expect_success(operation="get_data_source", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_source(self, data_source_id: int) -> DataSource:
        """Get Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            DataSource: Get a data source
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_get_data_source.sync_detailed(data_source_id=data_source_id, client=self._client)
        return _expect_success(operation="get_data_source", response=response, success_statuses={200}, allow_none=False)

    async def get_data_source_async(self, data_source_id: int) -> DataSource:
        """Get Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            DataSource: Get a data source
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_get_data_source.asyncio_detailed(data_source_id=data_source_id, client=self._client)
        return _expect_success(operation="get_data_source", response=response, success_statuses={200}, allow_none=False)

    async def get_data_source_async_detailed(self, data_source_id: int) -> Response[DataSource]:
        """Get Data Source
        
        Args:
            data_source_id (int, required): Data source ID
        
        Returns:
            Response[DataSource]: Get a data source. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_get_data_source.asyncio_detailed(data_source_id=data_source_id, client=self._client)
        parsed = _expect_success(operation="get_data_source", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_sources_detailed(self, *, project_id: int, limit: int | Unset = UNSET) -> Response[list[DataSource]]:
        """Get Data Sources
        
        Args:
            project_id (int, required): Filter by project ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSource]]: List data sources. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_get_data_sources.sync_detailed(project_id=project_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_sources", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_sources(self, *, project_id: int, limit: int | Unset = UNSET) -> list[DataSource]:
        """Get Data Sources
        
        Args:
            project_id (int, required): Filter by project ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSource]: List data sources
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = data_source_get_data_sources.sync_detailed(project_id=project_id, limit=limit, client=self._client)
        return _expect_success(operation="get_data_sources", response=response, success_statuses={200}, allow_none=False)

    async def get_data_sources_async(self, *, project_id: int, limit: int | Unset = UNSET) -> list[DataSource]:
        """Get Data Sources
        
        Args:
            project_id (int, required): Filter by project ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSource]: List data sources
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_get_data_sources.asyncio_detailed(project_id=project_id, limit=limit, client=self._client)
        return _expect_success(operation="get_data_sources", response=response, success_statuses={200}, allow_none=False)

    async def get_data_sources_async_detailed(self, *, project_id: int, limit: int | Unset = UNSET) -> Response[list[DataSource]]:
        """Get Data Sources
        
        Args:
            project_id (int, required): Filter by project ID
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSource]]: List data sources. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await data_source_get_data_sources.asyncio_detailed(project_id=project_id, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_sources", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_data_source_detailed(self, data_source_id: int, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> Response[DataSource]:
        """Update Data Source
        
        Flattened convenience method that builds UpdateDataSourceRequest internally.
        """
        body = UpdateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = data_source_update_data_source.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_data_source", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def update_data_source(self, data_source_id: int, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> DataSource:
        """Update Data Source
        
        Flattened convenience method that builds UpdateDataSourceRequest internally.
        """
        body = UpdateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = data_source_update_data_source.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="update_data_source", response=response, success_statuses={200}, allow_none=False)

    async def update_data_source_async(self, data_source_id: int, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> DataSource:
        """Update Data Source
        
        Flattened convenience method that builds UpdateDataSourceRequest internally.
        """
        body = UpdateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = await data_source_update_data_source.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="update_data_source", response=response, success_statuses={200}, allow_none=False)

    async def update_data_source_async_detailed(self, data_source_id: int, *, db_connection_id: int, kind: StableDataSourceKind, modules: DataSourceModules, name: str, object_: DataSourceObject, report_empty_datasets: bool, snapshot_filter: str, snapshot_query: str) -> Response[DataSource]:
        """Update Data Source
        
        Flattened convenience method that builds UpdateDataSourceRequest internally.
        """
        body = UpdateDataSourceRequest(
            db_connection_id=db_connection_id,
            kind=kind,
            modules=modules,
            name=name,
            object_=object_,
            report_empty_datasets=report_empty_datasets,
            snapshot_filter=snapshot_filter,
            snapshot_query=snapshot_query,
        )
        response = await data_source_update_data_source.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="update_data_source", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class DbConnectionApi:
    """Db connection endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get_db_connection_detailed(self, db_connection_id: int) -> Response[DbConnection]:
        """Get Db Connection
        
        Args:
            db_connection_id (int, required): Db connection ID
        
        Returns:
            Response[DbConnection]: Get a db connection. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = db_connection_get_db_connection.sync_detailed(db_connection_id=db_connection_id, client=self._client)
        parsed = _expect_success(operation="get_db_connection", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_db_connection(self, db_connection_id: int) -> DbConnection:
        """Get Db Connection
        
        Args:
            db_connection_id (int, required): Db connection ID
        
        Returns:
            DbConnection: Get a db connection
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = db_connection_get_db_connection.sync_detailed(db_connection_id=db_connection_id, client=self._client)
        return _expect_success(operation="get_db_connection", response=response, success_statuses={200}, allow_none=False)

    async def get_db_connection_async(self, db_connection_id: int) -> DbConnection:
        """Get Db Connection
        
        Args:
            db_connection_id (int, required): Db connection ID
        
        Returns:
            DbConnection: Get a db connection
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await db_connection_get_db_connection.asyncio_detailed(db_connection_id=db_connection_id, client=self._client)
        return _expect_success(operation="get_db_connection", response=response, success_statuses={200}, allow_none=False)

    async def get_db_connection_async_detailed(self, db_connection_id: int) -> Response[DbConnection]:
        """Get Db Connection
        
        Args:
            db_connection_id (int, required): Db connection ID
        
        Returns:
            Response[DbConnection]: Get a db connection. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await db_connection_get_db_connection.asyncio_detailed(db_connection_id=db_connection_id, client=self._client)
        parsed = _expect_success(operation="get_db_connection", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_db_connections_detailed(self, *, limit: int | Unset = UNSET) -> Response[list[DbConnection]]:
        """Get Db Connections
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DbConnection]]: List db connections. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = db_connection_get_db_connections.sync_detailed(limit=limit, client=self._client)
        parsed = _expect_success(operation="get_db_connections", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_db_connections(self, *, limit: int | Unset = UNSET) -> list[DbConnection]:
        """Get Db Connections
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DbConnection]: List db connections
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = db_connection_get_db_connections.sync_detailed(limit=limit, client=self._client)
        return _expect_success(operation="get_db_connections", response=response, success_statuses={200}, allow_none=False)

    async def get_db_connections_async(self, *, limit: int | Unset = UNSET) -> list[DbConnection]:
        """Get Db Connections
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DbConnection]: List db connections
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await db_connection_get_db_connections.asyncio_detailed(limit=limit, client=self._client)
        return _expect_success(operation="get_db_connections", response=response, success_statuses={200}, allow_none=False)

    async def get_db_connections_async_detailed(self, *, limit: int | Unset = UNSET) -> Response[list[DbConnection]]:
        """Get Db Connections
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DbConnection]]: List db connections. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await db_connection_get_db_connections.asyncio_detailed(limit=limit, client=self._client)
        parsed = _expect_success(operation="get_db_connections", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class InspectionRequestApi:
    """Inspection request endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get_inspection_request_detailed(self, inspection_request_id: int) -> Response[InspectionRequestStatusResponse]:
        """Get Inspection Request
        
        Args:
            inspection_request_id (int, required): Inspection request ID
        
        Returns:
            Response[InspectionRequestStatusResponse]: Inspection request status. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_request_get_inspection_request.sync_detailed(inspection_request_id=inspection_request_id, client=self._client)
        parsed = _expect_success(operation="get_inspection_request", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_inspection_request(self, inspection_request_id: int) -> InspectionRequestStatusResponse:
        """Get Inspection Request
        
        Args:
            inspection_request_id (int, required): Inspection request ID
        
        Returns:
            InspectionRequestStatusResponse: Inspection request status
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_request_get_inspection_request.sync_detailed(inspection_request_id=inspection_request_id, client=self._client)
        return _expect_success(operation="get_inspection_request", response=response, success_statuses={200}, allow_none=False)

    async def get_inspection_request_async(self, inspection_request_id: int) -> InspectionRequestStatusResponse:
        """Get Inspection Request
        
        Args:
            inspection_request_id (int, required): Inspection request ID
        
        Returns:
            InspectionRequestStatusResponse: Inspection request status
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_request_get_inspection_request.asyncio_detailed(inspection_request_id=inspection_request_id, client=self._client)
        return _expect_success(operation="get_inspection_request", response=response, success_statuses={200}, allow_none=False)

    async def get_inspection_request_async_detailed(self, inspection_request_id: int) -> Response[InspectionRequestStatusResponse]:
        """Get Inspection Request
        
        Args:
            inspection_request_id (int, required): Inspection request ID
        
        Returns:
            Response[InspectionRequestStatusResponse]: Inspection request status. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_request_get_inspection_request.asyncio_detailed(inspection_request_id=inspection_request_id, client=self._client)
        parsed = _expect_success(operation="get_inspection_request", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def submit_inspection_request_detailed(self, *, project_id: int, data_source_ids: list[int], include_all_data_sources: bool, mode: StableInspectionRequestMode, start_date: datetime.date, end_date: datetime.date, monthly_mode_days: list[int], weekly_mode_weekdays: list[int], use_notification: bool, inspection_job_id: int | None | Unset = UNSET) -> Response[None]:
        """Submit Inspection Request
        
        Flattened convenience method that builds SubmitInspectionRequest internally.
        """
        body = SubmitInspectionRequest(
            project_id=project_id,
            data_source_ids=data_source_ids,
            include_all_data_sources=include_all_data_sources,
            mode=mode,
            start_date=start_date,
            end_date=end_date,
            monthly_mode_days=monthly_mode_days,
            weekly_mode_weekdays=weekly_mode_weekdays,
            use_notification=use_notification,
            inspection_job_id=inspection_job_id,
        )
        response = inspection_request_submit_inspection_request.sync_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="submit_inspection_request", response=response, success_statuses={204}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def submit_inspection_request(self, *, project_id: int, data_source_ids: list[int], include_all_data_sources: bool, mode: StableInspectionRequestMode, start_date: datetime.date, end_date: datetime.date, monthly_mode_days: list[int], weekly_mode_weekdays: list[int], use_notification: bool, inspection_job_id: int | None | Unset = UNSET) -> None:
        """Submit Inspection Request
        
        Flattened convenience method that builds SubmitInspectionRequest internally.
        """
        body = SubmitInspectionRequest(
            project_id=project_id,
            data_source_ids=data_source_ids,
            include_all_data_sources=include_all_data_sources,
            mode=mode,
            start_date=start_date,
            end_date=end_date,
            monthly_mode_days=monthly_mode_days,
            weekly_mode_weekdays=weekly_mode_weekdays,
            use_notification=use_notification,
            inspection_job_id=inspection_job_id,
        )
        response = inspection_request_submit_inspection_request.sync_detailed(body=body, client=self._client)
        return _expect_success(operation="submit_inspection_request", response=response, success_statuses={204}, allow_none=False)

    async def submit_inspection_request_async(self, *, project_id: int, data_source_ids: list[int], include_all_data_sources: bool, mode: StableInspectionRequestMode, start_date: datetime.date, end_date: datetime.date, monthly_mode_days: list[int], weekly_mode_weekdays: list[int], use_notification: bool, inspection_job_id: int | None | Unset = UNSET) -> None:
        """Submit Inspection Request
        
        Flattened convenience method that builds SubmitInspectionRequest internally.
        """
        body = SubmitInspectionRequest(
            project_id=project_id,
            data_source_ids=data_source_ids,
            include_all_data_sources=include_all_data_sources,
            mode=mode,
            start_date=start_date,
            end_date=end_date,
            monthly_mode_days=monthly_mode_days,
            weekly_mode_weekdays=weekly_mode_weekdays,
            use_notification=use_notification,
            inspection_job_id=inspection_job_id,
        )
        response = await inspection_request_submit_inspection_request.asyncio_detailed(body=body, client=self._client)
        return _expect_success(operation="submit_inspection_request", response=response, success_statuses={204}, allow_none=False)

    async def submit_inspection_request_async_detailed(self, *, project_id: int, data_source_ids: list[int], include_all_data_sources: bool, mode: StableInspectionRequestMode, start_date: datetime.date, end_date: datetime.date, monthly_mode_days: list[int], weekly_mode_weekdays: list[int], use_notification: bool, inspection_job_id: int | None | Unset = UNSET) -> Response[None]:
        """Submit Inspection Request
        
        Flattened convenience method that builds SubmitInspectionRequest internally.
        """
        body = SubmitInspectionRequest(
            project_id=project_id,
            data_source_ids=data_source_ids,
            include_all_data_sources=include_all_data_sources,
            mode=mode,
            start_date=start_date,
            end_date=end_date,
            monthly_mode_days=monthly_mode_days,
            weekly_mode_weekdays=weekly_mode_weekdays,
            use_notification=use_notification,
            inspection_job_id=inspection_job_id,
        )
        response = await inspection_request_submit_inspection_request.asyncio_detailed(body=body, client=self._client)
        parsed = _expect_success(operation="submit_inspection_request", response=response, success_statuses={204}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class InspectionStatusApi:
    """Operations for the 'inspection_status' tag."""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get_data_set_inspection_statuses_detailed(self, *, data_source_id: int, dataset_id: int | Unset = UNSET, start_date: str, end_date: str, data_volume_status: int | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> Response[list[DatasetInspectionStatus]]:
        """Get Data Set Inspection Statuses
        
        Args:
            data_source_id (int, required): Filter by data source ID
            dataset_id (int | Unset, optional): Filter by data set ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DatasetInspectionStatus]]: Get data set inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_data_set_inspection_statuses.sync_detailed(data_source_id=data_source_id, dataset_id=dataset_id, start_date=start_date, end_date=end_date, data_volume_status=data_volume_status, data_anomaly_status=data_anomaly_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_set_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_set_inspection_statuses(self, *, data_source_id: int, dataset_id: int | Unset = UNSET, start_date: str, end_date: str, data_volume_status: int | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> list[DatasetInspectionStatus]:
        """Get Data Set Inspection Statuses
        
        Args:
            data_source_id (int, required): Filter by data source ID
            dataset_id (int | Unset, optional): Filter by data set ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DatasetInspectionStatus]: Get data set inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_data_set_inspection_statuses.sync_detailed(data_source_id=data_source_id, dataset_id=dataset_id, start_date=start_date, end_date=end_date, data_volume_status=data_volume_status, data_anomaly_status=data_anomaly_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        return _expect_success(operation="get_data_set_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_data_set_inspection_statuses_async(self, *, data_source_id: int, dataset_id: int | Unset = UNSET, start_date: str, end_date: str, data_volume_status: int | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> list[DatasetInspectionStatus]:
        """Get Data Set Inspection Statuses
        
        Args:
            data_source_id (int, required): Filter by data source ID
            dataset_id (int | Unset, optional): Filter by data set ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DatasetInspectionStatus]: Get data set inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_data_set_inspection_statuses.asyncio_detailed(data_source_id=data_source_id, dataset_id=dataset_id, start_date=start_date, end_date=end_date, data_volume_status=data_volume_status, data_anomaly_status=data_anomaly_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        return _expect_success(operation="get_data_set_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_data_set_inspection_statuses_async_detailed(self, *, data_source_id: int, dataset_id: int | Unset = UNSET, start_date: str, end_date: str, data_volume_status: int | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> Response[list[DatasetInspectionStatus]]:
        """Get Data Set Inspection Statuses
        
        Args:
            data_source_id (int, required): Filter by data source ID
            dataset_id (int | Unset, optional): Filter by data set ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DatasetInspectionStatus]]: Get data set inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_data_set_inspection_statuses.asyncio_detailed(data_source_id=data_source_id, dataset_id=dataset_id, start_date=start_date, end_date=end_date, data_volume_status=data_volume_status, data_anomaly_status=data_anomaly_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_set_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_source_inspection_statuses_detailed(self, *, project_id: int | Unset = UNSET, data_source_id: int | Unset = UNSET, start_date: str, end_date: str, data_source_name_like: str | Unset = UNSET, is_inspected: bool | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_volume_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> Response[list[DataSourceInspectionStatus]]:
        """Get Data Source Inspection Statuses
        
        Args:
            project_id (int | Unset, optional): Filter by project ID
            data_source_id (int | Unset, optional): Filter by data source ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_source_name_like (str | Unset, optional): Filter by data source name
            is_inspected (bool | Unset, optional): Filter by inspected state
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSourceInspectionStatus]]: Get data source inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_data_source_inspection_statuses.sync_detailed(project_id=project_id, data_source_id=data_source_id, start_date=start_date, end_date=end_date, data_source_name_like=data_source_name_like, is_inspected=is_inspected, data_anomaly_status=data_anomaly_status, data_volume_status=data_volume_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_source_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_data_source_inspection_statuses(self, *, project_id: int | Unset = UNSET, data_source_id: int | Unset = UNSET, start_date: str, end_date: str, data_source_name_like: str | Unset = UNSET, is_inspected: bool | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_volume_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> list[DataSourceInspectionStatus]:
        """Get Data Source Inspection Statuses
        
        Args:
            project_id (int | Unset, optional): Filter by project ID
            data_source_id (int | Unset, optional): Filter by data source ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_source_name_like (str | Unset, optional): Filter by data source name
            is_inspected (bool | Unset, optional): Filter by inspected state
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSourceInspectionStatus]: Get data source inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_data_source_inspection_statuses.sync_detailed(project_id=project_id, data_source_id=data_source_id, start_date=start_date, end_date=end_date, data_source_name_like=data_source_name_like, is_inspected=is_inspected, data_anomaly_status=data_anomaly_status, data_volume_status=data_volume_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        return _expect_success(operation="get_data_source_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_data_source_inspection_statuses_async(self, *, project_id: int | Unset = UNSET, data_source_id: int | Unset = UNSET, start_date: str, end_date: str, data_source_name_like: str | Unset = UNSET, is_inspected: bool | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_volume_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> list[DataSourceInspectionStatus]:
        """Get Data Source Inspection Statuses
        
        Args:
            project_id (int | Unset, optional): Filter by project ID
            data_source_id (int | Unset, optional): Filter by data source ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_source_name_like (str | Unset, optional): Filter by data source name
            is_inspected (bool | Unset, optional): Filter by inspected state
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[DataSourceInspectionStatus]: Get data source inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_data_source_inspection_statuses.asyncio_detailed(project_id=project_id, data_source_id=data_source_id, start_date=start_date, end_date=end_date, data_source_name_like=data_source_name_like, is_inspected=is_inspected, data_anomaly_status=data_anomaly_status, data_volume_status=data_volume_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        return _expect_success(operation="get_data_source_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_data_source_inspection_statuses_async_detailed(self, *, project_id: int | Unset = UNSET, data_source_id: int | Unset = UNSET, start_date: str, end_date: str, data_source_name_like: str | Unset = UNSET, is_inspected: bool | Unset = UNSET, data_anomaly_status: int | Unset = UNSET, data_volume_status: int | Unset = UNSET, data_validation_status: int | Unset = UNSET, data_analytics_status: int | Unset = UNSET, inspection_status: int | Unset = UNSET, limit: int | Unset = UNSET) -> Response[list[DataSourceInspectionStatus]]:
        """Get Data Source Inspection Statuses
        
        Args:
            project_id (int | Unset, optional): Filter by project ID
            data_source_id (int | Unset, optional): Filter by data source ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            data_source_name_like (str | Unset, optional): Filter by data source name
            is_inspected (bool | Unset, optional): Filter by inspected state
            data_anomaly_status (int | Unset, optional): Filter by data anomaly status
            data_volume_status (int | Unset, optional): Filter by data volume status
            data_validation_status (int | Unset, optional): Filter by data validation status
            data_analytics_status (int | Unset, optional): Filter by data analytics status
            inspection_status (int | Unset, optional): Filter by inspection status
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[DataSourceInspectionStatus]]: Get data source inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_data_source_inspection_statuses.asyncio_detailed(project_id=project_id, data_source_id=data_source_id, start_date=start_date, end_date=end_date, data_source_name_like=data_source_name_like, is_inspected=is_inspected, data_anomaly_status=data_anomaly_status, data_volume_status=data_volume_status, data_validation_status=data_validation_status, data_analytics_status=data_analytics_status, inspection_status=inspection_status, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_data_source_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_project_inspection_statuses_detailed(self, *, project_id: int, start_date: str, end_date: str, limit: int | Unset = UNSET) -> Response[list[ProjectInspectionStatus]]:
        """Get Project Inspection Statuses
        
        Args:
            project_id (int, required): Project ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[ProjectInspectionStatus]]: Get project inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_project_inspection_statuses.sync_detailed(project_id=project_id, start_date=start_date, end_date=end_date, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_project_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_project_inspection_statuses(self, *, project_id: int, start_date: str, end_date: str, limit: int | Unset = UNSET) -> list[ProjectInspectionStatus]:
        """Get Project Inspection Statuses
        
        Args:
            project_id (int, required): Project ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[ProjectInspectionStatus]: Get project inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = inspection_status_get_project_inspection_statuses.sync_detailed(project_id=project_id, start_date=start_date, end_date=end_date, limit=limit, client=self._client)
        return _expect_success(operation="get_project_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_project_inspection_statuses_async(self, *, project_id: int, start_date: str, end_date: str, limit: int | Unset = UNSET) -> list[ProjectInspectionStatus]:
        """Get Project Inspection Statuses
        
        Args:
            project_id (int, required): Project ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[ProjectInspectionStatus]: Get project inspection statuses
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_project_inspection_statuses.asyncio_detailed(project_id=project_id, start_date=start_date, end_date=end_date, limit=limit, client=self._client)
        return _expect_success(operation="get_project_inspection_statuses", response=response, success_statuses={200}, allow_none=False)

    async def get_project_inspection_statuses_async_detailed(self, *, project_id: int, start_date: str, end_date: str, limit: int | Unset = UNSET) -> Response[list[ProjectInspectionStatus]]:
        """Get Project Inspection Statuses
        
        Args:
            project_id (int, required): Project ID
            start_date (str, required): Start date (YYYY-MM-DD)
            end_date (str, required): End date (YYYY-MM-DD)
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[ProjectInspectionStatus]]: Get project inspection statuses. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await inspection_status_get_project_inspection_statuses.asyncio_detailed(project_id=project_id, start_date=start_date, end_date=end_date, limit=limit, client=self._client)
        parsed = _expect_success(operation="get_project_inspection_statuses", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class ProjectApi:
    """Project management endpoints"""
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get_project_detailed(self, project_id: int) -> Response[Project]:
        """Get Project
        
        Args:
            project_id (int, required): Project ID
        
        Returns:
            Response[Project]: Get a project. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = project_get_project.sync_detailed(project_id=project_id, client=self._client)
        parsed = _expect_success(operation="get_project", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_project(self, project_id: int) -> Project:
        """Get Project
        
        Args:
            project_id (int, required): Project ID
        
        Returns:
            Project: Get a project
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = project_get_project.sync_detailed(project_id=project_id, client=self._client)
        return _expect_success(operation="get_project", response=response, success_statuses={200}, allow_none=False)

    async def get_project_async(self, project_id: int) -> Project:
        """Get Project
        
        Args:
            project_id (int, required): Project ID
        
        Returns:
            Project: Get a project
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await project_get_project.asyncio_detailed(project_id=project_id, client=self._client)
        return _expect_success(operation="get_project", response=response, success_statuses={200}, allow_none=False)

    async def get_project_async_detailed(self, project_id: int) -> Response[Project]:
        """Get Project
        
        Args:
            project_id (int, required): Project ID
        
        Returns:
            Response[Project]: Get a project. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await project_get_project.asyncio_detailed(project_id=project_id, client=self._client)
        parsed = _expect_success(operation="get_project", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_projects_detailed(self, *, limit: int | Unset = UNSET) -> Response[list[Project]]:
        """Get Projects
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[Project]]: List projects. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = project_get_projects.sync_detailed(limit=limit, client=self._client)
        parsed = _expect_success(operation="get_projects", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)

    def get_projects(self, *, limit: int | Unset = UNSET) -> list[Project]:
        """Get Projects
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[Project]: List projects
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = project_get_projects.sync_detailed(limit=limit, client=self._client)
        return _expect_success(operation="get_projects", response=response, success_statuses={200}, allow_none=False)

    async def get_projects_async(self, *, limit: int | Unset = UNSET) -> list[Project]:
        """Get Projects
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            list[Project]: List projects
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await project_get_projects.asyncio_detailed(limit=limit, client=self._client)
        return _expect_success(operation="get_projects", response=response, success_statuses={200}, allow_none=False)

    async def get_projects_async_detailed(self, *, limit: int | Unset = UNSET) -> Response[list[Project]]:
        """Get Projects
        
        Args:
            limit (int | Unset, optional): Maximum number of rows to return (default: 200, max: 5000)
        
        Returns:
            Response[list[Project]]: List projects. Includes response metadata (status code and headers).
        
        Raises:
            NotFoundError: Raised when the endpoint returns 404 or no payload where a payload is expected.
            ApiResponseError: Raised when the endpoint returns a documented ApiError payload.
            errors.UnexpectedStatus: Raised when the API returns an undocumented status code and client.raise_on_unexpected_status is True.
            httpx.TimeoutException: Raised when the request exceeds the configured client timeout.
        """
        response = await project_get_projects.asyncio_detailed(limit=limit, client=self._client)
        parsed = _expect_success(operation="get_projects", response=response, success_statuses={200}, allow_none=False)
        return Response(status_code=response.status_code, content=response.content, headers=response.headers, parsed=parsed)


class DignaClient:
    """Entry point exposing one attribute per Digna area."""

    def __init__(
        self,
        base_url: str | AuthenticatedClient,
        token: str | None = None,
        *,
        raise_on_unexpected_status: bool = True,
        **client_kwargs: Any,
    ) -> None:
        if isinstance(base_url, AuthenticatedClient):
            self._client = base_url
        else:
            if token is None:
                raise ValueError("token is required when constructing DignaClient from base_url")
            self._client = AuthenticatedClient(
                base_url=base_url,
                token=token,
                raise_on_unexpected_status=raise_on_unexpected_status,
                **client_kwargs,
            )
        self.attribute: AttributeApi = AttributeApi(self._client)
        self.check_definition: CheckDefinitionApi = CheckDefinitionApi(self._client)
        self.data_set: DataSetApi = DataSetApi(self._client)
        self.data_source: DataSourceApi = DataSourceApi(self._client)
        self.db_connection: DbConnectionApi = DbConnectionApi(self._client)
        self.inspection_request: InspectionRequestApi = InspectionRequestApi(self._client)
        self.inspection_status: InspectionStatusApi = InspectionStatusApi(self._client)
        self.project: ProjectApi = ProjectApi(self._client)
