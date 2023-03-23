from typing import Optional
import pandas as pd
from zope.interface import Interface


class IDataExtractor(Interface):
    """
    Extractor objects are used to connect to external sources and get data.
    """

    def get_data(self, chunk_size: Optional[int] = None) -> pd.DataFrame:
        pass
