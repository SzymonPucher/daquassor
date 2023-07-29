from abc import ABC, abstractmethod
from typing import List

from common.models.workflow_config import WorkflowConfig


class IWorkflowConfigurationRepository(ABC):
    @abstractmethod
    def get_workflows(self) -> List[WorkflowConfig]:
        """Gets all workflows."""
        pass

    @abstractmethod
    def get_workflow(self, workflow_id: str) -> WorkflowConfig:
        """Gets given workflow."""
        pass

    @abstractmethod
    def add_workflow(self, new_workflow: WorkflowConfig) -> None:
        """Adds given workflow."""
        pass

    @abstractmethod
    def update_workflow(self, updated_workflow: WorkflowConfig) -> None:
        """Updates given workflow."""
        pass

    @abstractmethod
    def delete_workflow(self, workflow_id: str) -> None:
        """Deletes given workflow."""
        pass
