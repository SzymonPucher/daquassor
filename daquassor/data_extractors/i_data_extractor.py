from abc import abstractmethod, ABC
from typing import Optional

import pandas as pd


class ITabularDataExtractor(ABC):
    """Extractor objects are used to extract data from external tabular data sources."""

    @abstractmethod
    def get_data(self, chunk_size: Optional[int] = None) -> pd.DataFrame:
        pass
