from pathlib import Path
from confz import ConfZ, ConfZFileSource


class Config(ConfZ):
    db_connection_url: str
    jwt_secret: str
    jwt_algorithm: str
    encryption_key: str

    CONFIG_SOURCES = ConfZFileSource(
        file=Path(Path(__file__).parent.absolute(), "config.json")
    )
