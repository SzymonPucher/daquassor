from fastapi import Request

from api.models.api_response import APIResponse


def initialize_exception_handlers(app):
    @app.exception_handler(ValueError)
    async def value_error_exception_handler(request: Request, exc: ValueError):
        return APIResponse(status_code=400, message=f"Error: {exc}")
