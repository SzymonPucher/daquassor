from zope import component

from data_extractors import register_data_extractors
from data_extractors.i_tabular_data_extractor import ITabularDataExtractor

register_data_extractors()


def get_default_data_extractors():
    default_data_extractors = [
        (
            "csv_file_data_extractor",
            dict(file_path=r"tests\integration\data\example.csv"),
        )
    ]

    extractors = []
    for extractor_id, kwargs in default_data_extractors:
        extractor = component.queryUtility(ITabularDataExtractor, extractor_id)

        if extractor is None:
            raise LookupError(
                f"Data Extractor with id {extractor_id} does not exist. Make sure you installed it."
            )

        extractors.append(extractor(**kwargs))

    return extractors
