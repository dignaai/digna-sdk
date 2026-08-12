from enum import Enum

class StableDbConnectionTechnology(str, Enum):
    DATABRICKS = "databricks"
    HIVE = "hive"
    NETEZZA = "netezza"
    ORACLE = "oracle"
    POSTGRES = "postgres"
    SNOWFLAKE = "snowflake"
    SQLSERVER = "sqlserver"
    TERADATA = "teradata"

    def __str__(self) -> str:
        return str(self.value)
