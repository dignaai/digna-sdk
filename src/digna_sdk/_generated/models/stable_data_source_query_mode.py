from enum import StrEnum


class StableDataSourceQueryMode(StrEnum):
    COMBINED = "combined"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
