from fastapi import FastAPI
from daquassor.rest_api.routers import auth
import uvicorn

app = FastAPI()
app.include_router(auth.router)


def run_api(port: int = 5005):
    uvicorn.run("rest_api:app", host="0.0.0.0", port=int(port))
