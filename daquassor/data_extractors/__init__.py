from common.factories.global_components import component_classes
from .csv_file_data_extractor import CsvFileDataExtractor
from .static_tabular_data_extractor import StaticTabularDataExtractor


def register_data_extractors():
    component_classes.update(
        dict(static_tabular=StaticTabularDataExtractor, csv_file=CsvFileDataExtractor)
    )
