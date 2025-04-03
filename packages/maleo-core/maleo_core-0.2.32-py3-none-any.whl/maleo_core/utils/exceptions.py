from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from maleo_core.models.base.schemas.responses.general import BaseGeneralResponsesSchemas

class BaseExceptions:
    @staticmethod
    async def validation_exception_handler(request:Request, exc:RequestValidationError):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=BaseGeneralResponsesSchemas.ValidationError(other=exc.errors()).model_dump())

    @staticmethod
    async def http_exception_handler(request:Request, exc:StarletteHTTPException):
        if exc.status_code == 404:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=BaseGeneralResponsesSchemas.NotFoundError().model_dump())

        #* Handle other HTTP exceptions normally
        return None