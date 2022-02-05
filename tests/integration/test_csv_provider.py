from pydantic import ValidationError
import pytest
from daquassor.providers.csv import CsvProvider
import pandas as pd


file_path = 'tests/integration/data/example.csv'

@pytest.mark.parametrize('file_path, delimiter, quote_char, expected_error', [
    ('file_path_1.csv', ',', '"', None),
    (pd.DataFrame(), ',', '"', ValidationError),
    ('file_path_1.csv', [','], '"', ValidationError),
    ('file_path_1.csv', ',', ('"', ), ValidationError),
    (123, ',', '"', ValidationError),
    ('file_path_1.csv', 37, '"', None),  # numeric value can potentially be a delimiter, although it's confusing
    ('file_path_1.csv', ',', 6543, None)  # same goes for quote_char
])
def test_inititation(file_path, delimiter, quote_char, expected_error):
    # ACT
    if expected_error:
        with pytest.raises(expected_error):
            CsvProvider(file_path=file_path, delimiter=delimiter, quote_char=quote_char)
    else:
        CsvProvider(file_path=file_path, delimiter=delimiter, quote_char=quote_char)


def test_reading_csv():
    # ARRANGE
    csv_provider = CsvProvider(file_path=file_path)

    # ACT
    data = csv_provider.get_data()

    # ASSERT
    expected_result = {'name': {0: 'Mark', 1: 'James'}, 'age': {0: 22, 1: 30}}
    assert data.to_dict() == expected_result


def test_writing_csv():
    # ARRANGE
    csv_provider = CsvProvider(file_path=file_path)
    example = pd.DataFrame({'name': {0: 'Mark', 1: 'James'}, 'age': {0: 22, 1: 30}})

    # ACT
    csv_provider.send_data(example)

    # ASSERT
    with open(csv_provider.file_path, 'r') as f:
        data_from_file = f.read()
    
    assert data_from_file.split() == ['name,age', 'Mark,22', 'James,30']

