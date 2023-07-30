from abc import abstractmethod, ABC

import networkx as nx


class IGraphDataExtractor(ABC):
    """Extractor objects are used to extract data from graph data sources."""

    @abstractmethod
    def get_data(self) -> nx.Graph:
        pass
