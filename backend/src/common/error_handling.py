from starlette.responses import JSONResponse
from starlette.requests import Request

from .errors import InsertDuplicateInstanceException


def duplicate_key_error_handler(_: Request, error: InsertDuplicateInstanceException) -> JSONResponse:
    return JSONResponse(
        {
            "error": error.details,
            "location": error.location
        },
        status_code=error.code
    )
