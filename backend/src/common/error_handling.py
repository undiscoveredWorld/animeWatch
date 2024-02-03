from starlette.responses import JSONResponse
from starlette.requests import Request

from .errors import InsertDuplicateInstanceException, TimeOutException


def duplicate_key_error_handler(_: Request, error: InsertDuplicateInstanceException) -> JSONResponse:
    return JSONResponse(
        content={
            "error": error.details,
            "location": error.location
        },
        status_code=error.code
    )


def mongo_db_timeout_error_handler(_: Request, error: TimeOutException) -> JSONResponse:
    return JSONResponse(
        content={
            "error": error.details,
        },
        status_code=error.code
    )
