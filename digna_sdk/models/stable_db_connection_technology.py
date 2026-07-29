from enum import Enum

class StableDbConnectionTechnology(str, Enum):
    DATABRICKS = "databricks"
    ORACLE = "oracle"
    POSTGRES = "postgres"
    SQLSERVER = "sqlserver"

    def __str__(self) -> str:
        return str(self.value)
