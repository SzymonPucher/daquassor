import typer

from factories.data_extractors_factory import get_default_data_extractors
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


@app.command()
def assess():
    obj = get_default_data_extractors()
    for ext in obj:
        print(ext.get_data())


if __name__ == "__main__":
    app()
