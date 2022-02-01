from daquassor.providers.i_provider import IProvider
import pandas as pd


class CsvProvider(IProvider):
    def __init__(self, file_path: str, delimiter: str = ',', quote_char: str = '"') -> None:
        super().__init__()
        self.file_path = file_path
        self.delimiter = delimiter
        self.quote_char = quote_char

    def connect(self) -> None:
        pass

    def get_data(self, chunk_size: int = None) -> pd.DataFrame:
        return pd.read_csv(self.file_path, delimiter=self.delimiter, quotechar=self.quote_char, chunksize=chunk_size)

    def send_data(self, data: pd.DataFrame) -> None:
        data.to_csv(self.file_path, sep=self.delimiter, quotechar=self.quote_char, index=False)

    def close(self) -> None:
        pass
