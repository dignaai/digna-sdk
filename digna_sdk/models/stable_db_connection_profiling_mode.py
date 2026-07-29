from enum import Enum

class StableDbConnectionProfilingMode(str, Enum):
    PERMANENT = "permanent"
    SESSION = "session"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
