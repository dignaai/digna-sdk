"""Public, pydantic-based domain models for the Digna SDK.

These mirror the shapes returned by the Digna stable API. They are built by
validating the dictionaries produced by the generated (attrs-based) client
models, so field names and types match the OpenAPI spec exactly.
"""

from __future__ import annotations

import datetime

from pydantic import BaseModel, ConfigDict, Field

# Re-export the enums from the generated client so callers only ever need to
# import from `digna_sdk`, never from `digna_sdk._generated`. The OpenAPI spec
# does not document these enums beyond their member names, so we attach richer
# docstrings here (this mutates the enum classes' `__doc__` in place; it does
# not change their identity/values, so isinstance checks are unaffected).
from ._generated.models.api_error_code import ApiErrorCode
from ._generated.models.inspection_status import InspectionStatus
from ._generated.models.stable_attribute_category import StableAttributeCategory
from ._generated.models.stable_data_set_kind import StableDataSetKind
from ._generated.models.stable_data_source_kind import StableDataSourceKind
from ._generated.models.stable_data_source_query_mode import StableDataSourceQueryMode
from ._generated.models.stable_db_connection_profiling_mode import (
    StableDbConnectionProfilingMode,
)
from ._generated.models.stable_db_connection_technology import StableDbConnectionTechnology
from ._generated.models.stable_inspection_operation_status import StableInspectionOperationStatus
from ._generated.models.stable_inspection_request_mode import StableInspectionRequestMode
from ._generated.models.stable_inspection_request_weekday import StableInspectionRequestWeekday
from ._generated.models.test_status import TestStatus

ApiErrorCode.__doc__ = "Machine-readable error code returned in `ApiError.code`."
InspectionStatus.__doc__ = (
    "Overall daily inspection status for a project, data source, or dataset.\n\n"
    "Not formally documented by the API; based on observed data, `-1` means the "
    "entity was not inspected on that date, `0` means it was inspected without "
    "issues, `1` means warnings/uncertain results, and `2` means failures were "
    "detected."
)
StableAttributeCategory.__doc__ = "How an attribute's values should be treated statistically."
StableDataSetKind.__doc__ = (
    "Whether a dataset's rows are fixed (`STATIC`), determined by a live "
    "grouping expression (`DYNAMIC`), or both (`HYBRID`)."
)
StableDataSourceKind.__doc__ = (
    "Whether a data source is backed by a `TABLE`, a `VIEW`, or a custom `QUERY`."
)
StableDataSourceQueryMode.__doc__ = (
    "Whether a data source's snapshots are queried individually (`SINGLE`) or "
    "combined into a single query (`COMBINED`)."
)
StableDbConnectionProfilingMode.__doc__ = (
    "How a database connection is used for profiling: a `STANDARD` per-query "
    "connection, a `SESSION`-scoped connection, or a `PERMANENT` connection."
)
StableDbConnectionTechnology.__doc__ = "The database technology a connection targets."
StableInspectionOperationStatus.__doc__ = (
    "Lifecycle status of a submitted inspection request/job, as returned by "
    "`InspectionRequestsResource.get_status`."
)
StableInspectionRequestMode.__doc__ = (
    "How an inspection request's date range should be scheduled: every day, "
    "specific weekdays, or specific days of the month."
)
StableInspectionRequestWeekday.__doc__ = (
    "A weekday used with `StableInspectionRequestMode.WEEKLY`."
)
TestStatus.__doc__ = (
    "Outcome of a single check/metric within an inspection status (e.g. "
    "`InspectionMetric.status`).\n\n"
    "Not formally documented by the API; the value set mirrors `InspectionStatus` "
    "(`-1` not evaluated, `0` passed, `1` uncertain, `2` failed)."
)

__all__ = [
    "ApiErrorCode",
    "InspectionStatus",
    "StableAttributeCategory",
    "StableDataSetKind",
    "StableDataSourceKind",
    "StableDataSourceQueryMode",
    "StableDbConnectionProfilingMode",
    "StableDbConnectionTechnology",
    "StableInspectionOperationStatus",
    "StableInspectionRequestMode",
    "StableInspectionRequestWeekday",
    "TestStatus",
    "NamedRef",
    "DatasetRef",
    "StatisticRef",
    "InspectionMetric",
    "Project",
    "DbConnection",
    "DataSourceModules",
    "DataSourceObject",
    "DataSource",
    "DataSet",
    "AttributeCheckDefinition",
    "Attribute",
    "CheckDefinition",
    "InspectionRequestStatus",
    "SubmittedInspectionRequest",
    "DatasetInspectionStatus",
    "DataSourceInspectionStatus",
    "ProjectInspectionStatus",
]


class DignaModel(BaseModel):
    """Base class for all Digna SDK response models."""

    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class NamedRef(DignaModel):
    """A lightweight reference to another resource, as embedded in responses."""

    id: int = Field(description="ID of the referenced resource.")
    name: str = Field(description="Name of the referenced resource.")


class DatasetRef(NamedRef):
    """Reference to a dataset, including its fully-qualified name."""

    full_name: str = Field(description="Fully-qualified dataset name (e.g. including its group value).")


class StatisticRef(NamedRef):
    """Reference to a statistic."""

    macro_name: str = Field(description="The internal macro name used to compute this statistic.")


class InspectionMetric(DignaModel):
    """A generic pass/fail/uncertain test-outcome block used across inspection statuses.

    Not every field is populated for every metric kind (e.g. volume checks only
    set ``row_count``/``num_checks``, while validation/anomaly checks set
    ``num_passed``/``num_failed``/``num_uncertain``).
    """

    status: TestStatus = Field(description="Pass/fail/uncertain outcome for this metric.")
    num_passed: int | None = Field(default=None, description="Number of checks that passed.")
    num_failed: int | None = Field(default=None, description="Number of checks that failed.")
    num_uncertain: int | None = Field(
        default=None, description="Number of checks with an uncertain outcome."
    )
    num_checks: int | None = Field(default=None, description="Total number of checks evaluated.")
    num_not_relevant: int | None = Field(
        default=None, description="Number of checks that were not relevant/skipped."
    )
    row_count: int | None = Field(default=None, description="Row count observed for this metric.")


class Project(DignaModel):
    """A Digna project: the top-level container for data sources and datasets."""

    id: int = Field(description="Project ID.")
    name: str = Field(description="Project name.")
    description: str = Field(description="Project description.")
    db_connections: list[NamedRef] = Field(
        default=[], description="Database connections available to this project."
    )


class DbConnection(DignaModel):
    """A configured connection to a customer database."""

    id: int = Field(description="Db connection ID.")
    name: str = Field(description="Db connection name.")
    technology: StableDbConnectionTechnology = Field(description="The database technology.")
    profiling_mode: StableDbConnectionProfilingMode = Field(
        description="How this connection is used for profiling."
    )
    work_schema: str = Field(description="Schema used to store Digna's own working tables.")


class DataSourceModules(DignaModel):
    """Which inspection modules are enabled for a data source."""

    data_analytics: bool = Field(description="Whether data analytics checks are enabled.")
    data_anomaly: bool = Field(description="Whether data anomaly detection is enabled.")
    data_validation: bool = Field(description="Whether data validation checks are enabled.")
    schema_tracker: bool = Field(description="Whether schema change tracking is enabled.")
    timeliness: bool = Field(description="Whether timeliness/freshness checks are enabled.")


class DataSourceObject(DignaModel):
    """The catalog/schema/table location of a data source's underlying data."""

    catalog_name: str = Field(description="Database catalog name.")
    schema_name: str = Field(description="Database schema name.")
    table_name: str = Field(description="Table or view name.")


class DataSource(DignaModel):
    """A table, view, or query registered with Digna for inspection."""

    id: int = Field(description="Data source ID.")
    name: str = Field(description="Data source name.")
    kind: StableDataSourceKind = Field(description="Whether this is a table, view, or query.")
    query_mode: StableDataSourceQueryMode = Field(
        description="Whether snapshots are queried individually or combined."
    )
    project: NamedRef = Field(description="The project this data source belongs to.")
    db_connection: NamedRef = Field(
        description="The database connection used to query this data source."
    )
    modules: DataSourceModules = Field(description="Which inspection modules are enabled.")
    object: DataSourceObject = Field(description="The catalog/schema/table location of the data.")
    report_empty_datasets: bool = Field(
        description="Whether datasets that hold no rows are still reported."
    )
    snapshot_filter: str = Field(description="Row filter expression used to select a snapshot.")
    snapshot_query: str = Field(
        description="Custom query used instead of `object` when `kind` is `QUERY`."
    )


class DataSet(DignaModel):
    """A named subset of a data source, defined by filter/grouping expressions."""

    id: int = Field(description="Data set ID.")
    name: str = Field(description="Data set name.")
    kind: StableDataSetKind = Field(description="Whether the dataset is static, dynamic, or hybrid.")
    filter_expression: str = Field(description="Row filter expression applied to the data source.")
    grouping_expression: str = Field(
        description="Grouping expression used to split the data source into datasets."
    )
    project: NamedRef = Field(description="The project this dataset belongs to.")
    data_source: NamedRef = Field(description="The data source this dataset is derived from.")


class AttributeCheckDefinition(DignaModel):
    """A check definition generated for an attribute's statistic."""

    id: int = Field(description="Check definition ID.")
    statistic: NamedRef = Field(description="The statistic this check evaluates.")


class Attribute(DignaModel):
    """A monitored column of a data source."""

    id: int = Field(description="Attribute ID.")
    name: str = Field(description="Attribute name.")
    data_type: str = Field(description="The underlying column data type (e.g. `double precision`).")
    category: StableAttributeCategory = Field(
        description="How the attribute's values should be treated statistically."
    )
    project: NamedRef = Field(description="The project this attribute belongs to.")
    data_source: NamedRef = Field(description="The data source this attribute belongs to.")
    check_definitions: list[AttributeCheckDefinition] = Field(
        default=[], description="Check definitions generated for this attribute's statistics."
    )


class CheckDefinition(DignaModel):
    """A single automated check (e.g. row count, anomaly detection) on a data source or attribute."""

    id: int = Field(description="Check definition ID.")
    project: NamedRef = Field(description="The project this check belongs to.")
    data_source: NamedRef = Field(description="The data source this check runs against.")
    statistic: StatisticRef = Field(description="The statistic this check evaluates.")
    attribute: NamedRef | None = Field(
        default=None, description="The attribute this check applies to, if any (`None` for data-source-level checks)."
    )
    data_anomaly_enabled: bool = Field(description="Whether anomaly detection is enabled for this check.")
    lower_limit: float | None = Field(default=None, description="Fixed lower threshold, if configured.")
    upper_limit: float | None = Field(default=None, description="Fixed upper threshold, if configured.")
    min_threshold: float | None = Field(
        default=None, description="Minimum acceptable value learned/configured for anomaly detection."
    )
    max_threshold: float | None = Field(
        default=None, description="Maximum acceptable value learned/configured for anomaly detection."
    )


class InspectionRequestStatus(DignaModel):
    """The current lifecycle status of a submitted inspection request."""

    id: int = Field(description="Inspection request ID.")
    status: StableInspectionOperationStatus = Field(description="Current lifecycle status.")


class SubmittedInspectionRequest(DignaModel):
    """The identifier returned after submitting a new inspection request."""

    id: int = Field(description="Inspection request ID, used to poll `get_status`.")


class DatasetInspectionStatus(DignaModel):
    """The inspection outcome for a single dataset on a single day."""

    project: NamedRef = Field(description="The project the dataset belongs to.")
    data_source: NamedRef = Field(description="The data source the dataset belongs to.")
    dataset: DatasetRef = Field(description="The inspected dataset.")
    dataset_definition: NamedRef = Field(description="The dataset definition that produced this dataset.")
    status: InspectionStatus = Field(description="Overall inspection status for this day.")
    valid_date: datetime.date = Field(description="The day this status applies to.")
    data_volume_status: InspectionMetric | None = Field(
        default=None, description="Row-count/volume check outcome, if evaluated."
    )
    data_anomaly_status: InspectionMetric | None = Field(
        default=None, description="Anomaly detection outcome, if evaluated."
    )
    data_validation_status: InspectionMetric | None = Field(
        default=None, description="Data validation check outcome, if evaluated."
    )
    data_analytics_status: InspectionMetric | None = Field(
        default=None, description="Data analytics check outcome, if evaluated."
    )


class DataSourceInspectionStatus(DignaModel):
    """The inspection outcome for a whole data source on a single day."""

    project: NamedRef = Field(description="The project the data source belongs to.")
    data_source: NamedRef = Field(description="The inspected data source.")
    is_inspected: bool = Field(description="Whether the data source was actually inspected on this day.")
    status: InspectionStatus = Field(description="Overall inspection status for this day.")
    valid_date: datetime.date = Field(description="The day this status applies to.")
    inspected_at: datetime.datetime | None = Field(
        default=None, description="When the inspection ran, if it was inspected."
    )
    row_count: int | None = Field(
        default=None,
        description="Rows the data source held on `valid_date`, `None` for a date it was not profiled on.",
    )
    data_volume_status: InspectionMetric | None = Field(
        default=None, description="Row-count/volume check outcome, if evaluated."
    )
    data_anomaly_status: InspectionMetric | None = Field(
        default=None, description="Anomaly detection outcome, if evaluated."
    )
    data_validation_status: InspectionMetric | None = Field(
        default=None, description="Data validation check outcome, if evaluated."
    )
    data_analytics_status: InspectionMetric | None = Field(
        default=None, description="Data analytics check outcome, if evaluated."
    )


class ProjectInspectionStatus(DignaModel):
    """The aggregate inspection outcome for a whole project on a single day."""

    project: NamedRef = Field(description="The inspected project.")
    status: InspectionStatus = Field(description="Overall inspection status for this day.")
    valid_date: datetime.date = Field(description="The day this status applies to.")
