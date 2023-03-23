from zope import component

from data_extractors import register_data_extractors
from interfaces.i_data_extractor import IDataExtractor

register_data_extractors()


def get_default_data_extractors():
    default_data_extractors = [
        (
            "csv_file_data_extractor",
            dict(
                file_path=r"C:\Users\Nowy\Projekty\daquassor\tests\integration\data\example.csv"
            ),
        )
    ]

    extractors = []
    for extractor_id, kwargs in default_data_extractors:
        extractor = component.queryUtility(IDataExtractor, extractor_id)

        if extractor is None:
            raise LookupError(
                f"Data Extractor with id {extractor_id} does not exist. Make sure you installed it."
            )

        extractors.append(extractor(**kwargs))

    return extractors
