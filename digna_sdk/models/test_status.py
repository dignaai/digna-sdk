from enum import IntEnum

class TestStatus(IntEnum):
    VALUE_NEGATIVE_2 = -2
    VALUE_NEGATIVE_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

    def __str__(self) -> str:
        return str(self.value)
