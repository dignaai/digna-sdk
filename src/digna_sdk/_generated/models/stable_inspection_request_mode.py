from enum import StrEnum


class StableInspectionRequestMode(StrEnum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"

    def __str__(self) -> str:
        return str(self.value)
