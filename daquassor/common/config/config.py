from pathlib import Path
from confz import BaseConfig, FileSource


class Config(BaseConfig):
    db_connection_url: str

    CONFIG_SOURCES = FileSource(
        file=Path(Path(__file__).parent.absolute(), "config.json")
    )
