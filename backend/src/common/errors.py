"""
errors storages custom exceptions
"""
from typing import Any


class CustomExceptionBase(Exception):
    details: str
    code: int

    def __init__(self, details: str, code: int, *args):
        super().__init__(*args)
        self.details = details
        self.code = code


class LocatedException(CustomExceptionBase):
    location: dict[str, Any]

    def __init__(self, details: str, code: int, location: dict[str, Any], *args):
        super().__init__(details, code, *args)
        self.location = location


class InsertDuplicateInstanceException(LocatedException):
    pass


class TimeOutException(CustomExceptionBase):
    pass
