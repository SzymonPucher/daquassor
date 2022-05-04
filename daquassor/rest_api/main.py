import uvicorn
from fastapi import FastAPI

from daquassor.providers.config_provider import ConfigProvider
from daquassor.rest_api.handlers.exception_handlers import initialize_exception_handlers
from daquassor.rest_api.routers import auth
from daquassor.rest_api.services.db_structure_initialization_service import initialize_database

app = FastAPI()
app.include_router(auth.router)
initialize_exception_handlers(app)

config_provider = ConfigProvider()

if __name__ == "__main__":
    initialize_database()
    uvicorn.run("daquassor.rest_api.main:app", host="0.0.0.0", port=8081, reload=True)
