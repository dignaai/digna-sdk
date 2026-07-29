from enum import Enum

class StableDataSourceKind(str, Enum):
    QUERY = "QUERY"
    TABLE = "TABLE"
    VIEW = "VIEW"

    def __str__(self) -> str:
        return str(self.value)
