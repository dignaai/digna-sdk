from enum import StrEnum


class StableDataSetKind(StrEnum):
    DYNAMIC = "DYNAMIC"
    HYBRID = "HYBRID"
    STATIC = "STATIC"

    def __str__(self) -> str:
        return str(self.value)
