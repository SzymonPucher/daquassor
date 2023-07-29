from fastapi import FastAPI
from daquassor.rest_api.routers import ready
import uvicorn

app = FastAPI()
app.include_router(ready.router)


def run_api(port: int = 5005):
    uvicorn.run(app, host="0.0.0.0", port=int(port))
