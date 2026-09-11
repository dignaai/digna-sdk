from enum import StrEnum


class StableInspectionRequestWeekday(StrEnum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"

    def __str__(self) -> str:
        return str(self.value)
