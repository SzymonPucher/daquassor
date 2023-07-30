from abc import ABC, abstractmethod
from typing import List

import pandas as pd

from common.models.dataset_metric import DatasetMetric


class ITabularDatasetMetricCalculator(ABC):
    @abstractmethod
    def calculate_metric(
        self, data_source_id: str, dataset_id: str, data: pd.DataFrame
    ) -> List[DatasetMetric]:
        """Calculates metric of given dataset based on extracted data."""
        pass
