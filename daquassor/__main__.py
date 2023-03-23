import typer

from factories.data_extractors_factory import get_default_data_extractors

app = typer.Typer()


@app.command()
def init():
    print(f"Initiating application.")


@app.command()
def api(port=5005):
    print(f"Starting API on port {port}.")


@app.command()
def assess():
    obj = get_default_data_extractors()
    for ext in obj:
        print(ext.get_data())


if __name__ == "__main__":
    app()
