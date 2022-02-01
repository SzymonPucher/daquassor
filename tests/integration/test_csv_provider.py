from daquassor.providers.csv import CsvProvider
import pandas as pd


def test_reading_csv():
    # ARRANGE
    csv_provider = CsvProvider('tests/integration/data/example.csv')

    # ACT
    data = csv_provider.get_data()

    # ASSERT
    expected_result = {'name': {0: 'Mark', 1: 'James'}, 'age': {0: 22, 1: 30}}
    assert data.to_dict() == expected_result


def test_writing_csv():
    # ARRANGE
    csv_provider = CsvProvider('tests/integration/data/example.csv')
    example = pd.DataFrame({'name': {0: 'Mark', 1: 'James'}, 'age': {0: 22, 1: 30}})

    # ACT
    csv_provider.send_data(example)

    # ASSERT
    with open(csv_provider.file_path, 'r') as f:
        data_from_file = f.read()
    
    assert data_from_file.split() == ['name,age', 'Mark,22', 'James,30']

