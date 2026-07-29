from enum import Enum

class ApiErrorCode(str, Enum):
    BAD_REQUEST = "BAD_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    INVALID_LICENSE = "INVALID_LICENSE"
    NOT_AUTHENTICATED = "NOT_AUTHENTICATED"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
