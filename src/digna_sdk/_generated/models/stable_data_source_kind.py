from enum import StrEnum


class StableDataSourceKind(StrEnum):
    QUERY = "QUERY"
    TABLE = "TABLE"
    VIEW = "VIEW"

    def __str__(self) -> str:
        return str(self.value)
