from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.symbol_exceptions import DuplicateSymbolException


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DuplicateSymbolException)
    async def duplicate_symbol_exception_handler(
        request: Request,
        exc: DuplicateSymbolException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail": str(exc),
            },
        )