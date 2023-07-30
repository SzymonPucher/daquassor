from pydantic import ValidationError
import pytest
import pandas as pd

from data_extractors import CsvFileDataExtractor

file_path = "tests/integration/data/example.csv"


@pytest.mark.parametrize(
    "file_path, delimiter, quote_char, expected_error",
    [
        ("file_path_1.csv", ",", '"', None),
        (pd.DataFrame(), ",", '"', ValidationError),
        ("file_path_1.csv", [","], '"', ValidationError),
        ("file_path_1.csv", ",", ('"',), ValidationError),
        (123, ",", '"', ValidationError),
        ("file_path_1.csv", 37, '"', ValidationError),
        ("file_path_1.csv", ",", 6543, ValidationError),
    ],
)
def test_initiation(file_path, delimiter, quote_char, expected_error):
    # ACT
    if expected_error:
        with pytest.raises(expected_error):
            CsvFileDataExtractor(
                file_path=file_path, delimiter=delimiter, quote_char=quote_char
            )
    else:
        CsvFileDataExtractor(
            file_path=file_path, delimiter=delimiter, quote_char=quote_char
        )


def test_reading_csv():
    # ARRANGE
    csv_extractor = CsvFileDataExtractor(file_path=file_path)

    # ACT
    data = csv_extractor.get_data()

    # ASSERT
    expected_result = {"name": {0: "Mark", 1: "James"}, "age": {0: 22, 1: 30}}
    assert data.to_dict() == expected_result
