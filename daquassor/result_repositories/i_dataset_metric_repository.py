from abc import ABC, abstractmethod
from typing import Optional, List

from common.models.dataset_metric import DatasetMetric


class IDatasetMetricRepository(ABC):
    @abstractmethod
    def get_dataset_metrics(
        self,
        data_source_ids: Optional[List[str]],
        dataset_ids: Optional[List[str]],
        dataset_metric_ids: Optional[List[str]],
    ) -> List[DatasetMetric]:
        """Gets metrics matching provided parameters.
        In case of no arguments provided, all metrics for all datasets are returned.
        """
        pass

    @abstractmethod
    def get_dataset_metric(self, dataset_metric_id: str) -> DatasetMetric:
        """Gets given metric."""
        pass

    @abstractmethod
    def add_dataset_metric(self, new_dataset_metric: DatasetMetric) -> None:
        """Updates given metric."""
        pass

    @abstractmethod
    def update_dataset_metric(self, updated_dataset_metric: DatasetMetric) -> None:
        """Updates given metric."""
        pass

    @abstractmethod
    def delete_dataset_metric(self, dataset_metric_id: str) -> None:
        """Removes given metric."""
        pass

    @abstractmethod
    def delete_dataset_metrics(self, dataset_id: str) -> None:
        """Removes all metrics for given dataset."""
        pass

    @abstractmethod
    def delete_data_source_metrics(self, data_source_id: str) -> None:
        """Removes all metrics for given data_source."""
        pass
