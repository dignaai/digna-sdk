from enum import StrEnum


class StableDbConnectionTechnology(StrEnum):
    DATABRICKS = "databricks"
    HIVE = "hive"
    IMPALA = "impala"
    NETEZZA = "netezza"
    ORACLE = "oracle"
    POSTGRES = "postgres"
    SNOWFLAKE = "snowflake"
    SQLSERVER = "sqlserver"
    TERADATA = "teradata"

    def __str__(self) -> str:
        return str(self.value)
