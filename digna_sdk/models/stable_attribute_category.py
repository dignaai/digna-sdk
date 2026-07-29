from enum import Enum

class StableAttributeCategory(str, Enum):
    CATEGORICAL = "CATEGORICAL"
    CUSTOM = "CUSTOM"
    NUMERICAL = "NUMERICAL"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
