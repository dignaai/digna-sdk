"""Convenience access to `/v1/attributes`."""

from __future__ import annotations

from .._convert import to_model, to_model_list, unwrap
from .._generated.api.attributes import (
    create_attribute,
    delete_attribute,
    get_attribute,
    get_attributes,
    update_attribute,
)
from .._generated.client import AuthenticatedClient, Client
from .._generated.models.create_attribute_request import CreateAttributeRequest
from .._generated.models.stable_attribute_category import StableAttributeCategory
from .._generated.models.update_attribute_request import UpdateAttributeRequest
from .._generated.types import UNSET
from ..models import Attribute


class AttributesResource:
    """Resource client for `/v1/attributes`."""

    def __init__(self, client: AuthenticatedClient | Client) -> None:
        self._client = client

    def list(self, data_source_id: int, *, limit: int | None = None) -> list[Attribute]:
        """List attributes belonging to a data source.

        Args:
            data_source_id: Filter by data source ID.
            limit: Maximum number of rows to return (API default: 200, max: 5000).
        """
        response = get_attributes.sync_detailed(
            client=self._client,
            data_source_id=data_source_id,
            limit=limit if limit is not None else UNSET,
        )
        return to_model_list(Attribute, unwrap(response))

    def get(self, attribute_id: int) -> Attribute:
        """Get a single attribute by id.

        Args:
            attribute_id: Attribute ID.
        """
        response = get_attribute.sync_detailed(client=self._client, attribute_id=attribute_id)
        return to_model(Attribute, unwrap(response))

    def create(
        self,
        *,
        data_source_id: int,
        name: str,
        data_type: str,
        category: StableAttributeCategory,
        statistic_ids: list[int],
    ) -> Attribute:
        """Create a new attribute.

        Args:
            data_source_id: The data source this attribute belongs to.
            name: Attribute name.
            data_type: The underlying column data type (e.g. ``"double precision"``).
            category: How the attribute's values should be treated statistically.
            statistic_ids: IDs of the statistics to compute check definitions for.
        """
        body = CreateAttributeRequest(
            data_source_id=data_source_id,
            name=name,
            data_type=data_type,
            category=category,
            statistic_ids=statistic_ids,
        )
        response = create_attribute.sync_detailed(client=self._client, body=body)
        return to_model(Attribute, unwrap(response))

    def update(
        self,
        attribute_id: int,
        *,
        name: str,
        data_type: str,
        category: StableAttributeCategory,
        statistic_ids: list[int],
    ) -> Attribute:
        """Update an existing attribute.

        Args:
            attribute_id: Attribute ID.
            name: Attribute name.
            data_type: The underlying column data type (e.g. ``"double precision"``).
            category: How the attribute's values should be treated statistically.
            statistic_ids: IDs of the statistics to compute check definitions for.
        """
        body = UpdateAttributeRequest(
            name=name,
            data_type=data_type,
            category=category,
            statistic_ids=statistic_ids,
        )
        response = update_attribute.sync_detailed(
            client=self._client, attribute_id=attribute_id, body=body
        )
        return to_model(Attribute, unwrap(response))

    def delete(self, attribute_id: int) -> None:
        """Delete an attribute.

        Args:
            attribute_id: Attribute ID.
        """
        response = delete_attribute.sync_detailed(client=self._client, attribute_id=attribute_id)
        unwrap(response)
