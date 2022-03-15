from typing import Optional

import pandas as pd
from pydantic import BaseModel, StrictStr

from daquassor.providers.i_provider import IProvider


class CsvFileProvider(IProvider, BaseModel):
    file_path: StrictStr
    delimiter: Optional[str] = ','
    quote_char: Optional[str] = '"'

    def connect(self) -> None:
        pass

    def get_data(self, chunk_size: int = None) -> pd.DataFrame:
        return pd.read_csv(self.file_path, delimiter=self.delimiter, quotechar=self.quote_char, chunksize=chunk_size)

    def send_data(self, data: pd.DataFrame) -> None:
        data.to_csv(self.file_path, sep=self.delimiter, quotechar=self.quote_char, index=False)

    def close(self) -> None:
        pass
