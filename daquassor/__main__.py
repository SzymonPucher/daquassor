import typer

from rest_api import run_api
from rest_api.init_db import initialize_database

app = typer.Typer()


@app.command()
def init():
    print(f"Initiating application.")
    initialize_database()


@app.command()
def api(port=5005):
    print(f"Starting API on port {port}.")
    run_api(port)


if __name__ == "__main__":
    app()
