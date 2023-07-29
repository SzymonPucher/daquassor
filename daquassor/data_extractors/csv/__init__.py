from .csv_file_data_extractor import CsvFileDataExtractor
from data_extractors.i_tabular_data_extractor import ITabularDataExtractor
from zope import component

component.provideUtility(
    CsvFileDataExtractor, ITabularDataExtractor, "csv_file_data_extractor"
)
