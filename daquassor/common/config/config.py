from pathlib import Path
from confz import ConfZ, ConfZFileSource


class Config(ConfZ):
    db_connection_url: str

    CONFIG_SOURCES = ConfZFileSource(
        file=Path(Path(__file__).parent.absolute(), "config.json")
    )
