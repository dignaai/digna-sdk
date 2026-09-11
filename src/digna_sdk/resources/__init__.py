"""Pythonic, resource-oriented wrappers around the generated Digna API client."""

from .attributes import AttributesResource
from .check_definitions import CheckDefinitionsResource
from .data_sets import DataSetsResource
from .data_sources import DataSourcesResource
from .db_connections import DbConnectionsResource
from .inspection_requests import InspectionRequestsResource
from .inspection_statuses import InspectionStatusesResource
from .projects import ProjectsResource

__all__ = [
    "AttributesResource",
    "CheckDefinitionsResource",
    "DataSetsResource",
    "DataSourcesResource",
    "DbConnectionsResource",
    "InspectionRequestsResource",
    "InspectionStatusesResource",
    "ProjectsResource",
]
