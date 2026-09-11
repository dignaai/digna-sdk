from enum import StrEnum


class StableDbConnectionProfilingMode(StrEnum):
    PERMANENT = "permanent"
    SESSION = "session"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
