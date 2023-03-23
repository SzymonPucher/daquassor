from .csv_file_data_extractor import CsvFileDataExtractor
from interfaces.i_data_extractor import IDataExtractor
from zope import component

component.provideUtility(
    CsvFileDataExtractor, IDataExtractor, "csv_file_data_extractor"
)
