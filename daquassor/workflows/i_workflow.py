from abc import ABC, abstractmethod


class IWorkflow(ABC):
    @abstractmethod
    def run(self) -> None:
        """Runs the workflow."""
        pass
