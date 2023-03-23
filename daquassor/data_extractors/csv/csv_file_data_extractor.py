from typing import Optional

import pandas as pd
from pydantic import BaseModel, StrictStr
from zope.interface import implementer

from interfaces.i_data_extractor import IDataExtractor


@implementer(IDataExtractor)
class CsvFileDataExtractor(BaseModel):
    file_path: StrictStr
    delimiter: Optional[str] = ","
    quote_char: Optional[str] = '"'

    def get_data(self, chunk_size: Optional[int] = None) -> pd.DataFrame:
        return pd.read_csv(
            self.file_path,
            delimiter=self.delimiter,
            quotechar=self.quote_char,
            chunksize=chunk_size,
        )
