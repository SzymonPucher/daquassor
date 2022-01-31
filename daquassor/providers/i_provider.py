from abc import ABC
import pandas as pd


class IProvider(ABC):
    """
    Provider objects are used to connect to external sources and get data.
    """

    def connect(self) -> None:
        pass

    def get_data(self, chunk_size: int = None) -> pd.DataFrame:
        pass

    def send_data(self, data: pd.DataFrame) -> None:
        pass

    def close(self) -> None:
        pass
