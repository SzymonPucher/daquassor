from fastapi import Request

from rest_api.models.api_response import APIResponse


def initialize_exception_handlers(app):
    @app.exception_handler(ValueError)
    async def unicorn_exception_handler(request: Request, exc: ValueError):
        return APIResponse(status_code=400, message=f"Error: {exc}")
