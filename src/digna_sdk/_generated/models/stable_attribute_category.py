from enum import StrEnum


class StableAttributeCategory(StrEnum):
    CATEGORICAL = "CATEGORICAL"
    CUSTOM = "CUSTOM"
    NUMERICAL = "NUMERICAL"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
