"""Tests for the data sources, data sets, and attributes resources."""

from __future__ import annotations

import respx
from httpx import Response

from digna_sdk import DignaClient
from digna_sdk.models import (
    DataSourceModules,
    DataSourceObject,
    StableAttributeCategory,
    StableDataSetKind,
    StableDataSourceKind,
    StableDataSourceQueryMode,
)

from .conftest import BASE_URL

_DATA_SOURCE_JSON = {
    "id": 5,
    "name": "orders_table",
    "kind": "TABLE",
    "query_mode": "single",
    "project": {"id": 1, "name": "Sales"},
    "db_connection": {"id": 10, "name": "warehouse"},
    "modules": {
        "data_analytics": True,
        "data_anomaly": True,
        "data_validation": True,
        "schema_tracker": False,
        "timeliness": False,
    },
    "object": {"catalog_name": "prod", "schema_name": "public", "table_name": "orders"},
    "report_empty_datasets": False,
    "snapshot_filter": "",
    "snapshot_query": "",
}


@respx.mock
def test_list_data_sources(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/data-sources", params={"project_id": "1"}).mock(
        return_value=Response(200, json=[_DATA_SOURCE_JSON])
    )

    data_sources = client.data_sources.list(project_id=1)

    assert len(data_sources) == 1
    assert data_sources[0].object.table_name == "orders"
    assert data_sources[0].kind == StableDataSourceKind.TABLE


@respx.mock
def test_create_data_source(client: DignaClient) -> None:
    route = respx.post(f"{BASE_URL}/v1/data-sources").mock(
        return_value=Response(201, json=_DATA_SOURCE_JSON)
    )

    data_source = client.data_sources.create(
        project_id=1,
        db_connection_id=10,
        name="orders_table",
        kind=StableDataSourceKind.TABLE,
        query_mode=StableDataSourceQueryMode.SINGLE,
        object=DataSourceObject(catalog_name="prod", schema_name="public", table_name="orders"),
        modules=DataSourceModules(
            data_analytics=True,
            data_anomaly=True,
            data_validation=True,
            schema_tracker=False,
            timeliness=False,
        ),
    )

    assert route.called
    assert data_source.id == 5


@respx.mock
def test_list_data_sets(client: DignaClient) -> None:
    respx.get(f"{BASE_URL}/v1/data-sets", params={"data_source_id": "5"}).mock(
        return_value=Response(
            200,
            json=[
                {
                    "id": 7,
                    "name": "daily_orders",
                    "kind": "DYNAMIC",
                    "filter_expression": "",
                    "grouping_expression": "",
                    "project": {"id": 1, "name": "Sales"},
                    "data_source": {"id": 5, "name": "orders_table"},
                }
            ],
        )
    )

    data_sets = client.data_sets.list(data_source_id=5)

    assert data_sets[0].kind == StableDataSetKind.DYNAMIC


@respx.mock
def test_create_attribute(client: DignaClient) -> None:
    route = respx.post(f"{BASE_URL}/v1/attributes").mock(
        return_value=Response(
            201,
            json={
                "id": 9,
                "name": "amount",
                "data_type": "float",
                "category": "NUMERICAL",
                "project": {"id": 1, "name": "Sales"},
                "data_source": {"id": 5, "name": "orders_table"},
                "check_definitions": [],
            },
        )
    )

    attribute = client.attributes.create(
        data_source_id=5,
        name="amount",
        data_type="float",
        category=StableAttributeCategory.NUMERICAL,
        statistic_ids=[1, 2],
    )

    assert route.called
    assert attribute.category == StableAttributeCategory.NUMERICAL
