import pandas as pd
from pydantic import BaseModel, StrictStr

from daquassor.providers.i_data_provider import IDataProvider


class JsonFileDataProvider(IDataProvider, BaseModel):
    file_path: StrictStr

    def connect(self) -> None:
        pass

    def get_data(self, chunk_size: int = None) -> pd.DataFrame:
        return pd.read_json(self.file_path, chunksize=chunk_size)

    def send_data(self, data: pd.DataFrame) -> None:
        data.to_json(self.file_path, index=False)

    def close(self) -> None:
        pass
