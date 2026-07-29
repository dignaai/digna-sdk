from enum import Enum

class StableDataSetKind(str, Enum):
    DYNAMIC = "DYNAMIC"
    HYBRID = "HYBRID"
    STATIC = "STATIC"

    def __str__(self) -> str:
        return str(self.value)
