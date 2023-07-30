from abc import ABC, abstractmethod
from typing import Optional, List

from common.models.report import Report


class IDataQualityReportRepository(ABC):
    @abstractmethod
    def get_reports(
        self,
        data_source_ids: Optional[List[str]],
        dataset_ids: Optional[List[str]],
        report_ids: Optional[List[str]],
    ) -> List[Report]:
        """Gets reports matching provided parameters.
        In case of no arguments provided, all reports for all datasets are returned.
        """
        pass

    @abstractmethod
    def get_report(self, report_id: str) -> Report:
        """Gets given report."""
        pass

    @abstractmethod
    def add_report(self, new_report: Report) -> None:
        """Adds given report."""
        pass

    @abstractmethod
    def update_report(self, updated_report: Report) -> None:
        """Updates given report."""
        pass

    @abstractmethod
    def delete_report(self, report_id: str) -> None:
        """Deletes given report."""
        pass

    @abstractmethod
    def delete_dataset_reports(self, dataset_id: str) -> None:
        """Removes all reports for given dataset."""
        pass

    @abstractmethod
    def delete_data_source_reports(self, data_source_id: str) -> None:
        """Removes all reports for given data source."""
        pass
