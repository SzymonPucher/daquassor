from abc import ABC, abstractmethod
from typing import List

from common.models.dataset_metric import DatasetMetric
from common.models.report import Report


class IDataQualityAssessor(ABC):
    @abstractmethod
    def assess_quality(self, data_set_metrics: List[DatasetMetric]) -> Report:
        """Assess quality of given dataset based on collected metrics."""
        pass
