import json
from typing import Optional, Dict, List

import pandas as pd

from data_extractors.i_tabular_data_extractor import ITabularDataExtractor


class StaticTabularDataExtractor(ITabularDataExtractor):
    def __init__(self, data: str):
        self.json_data: List[Dict] = json.loads(data)

    def get_data(self, chunk_size: Optional[int] = None) -> pd.DataFrame:
        return pd.DataFrame(self.json_data)
