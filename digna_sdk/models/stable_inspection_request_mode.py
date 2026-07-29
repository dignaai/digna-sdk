from enum import Enum

class StableInspectionRequestMode(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"

    def __str__(self) -> str:
        return str(self.value)
