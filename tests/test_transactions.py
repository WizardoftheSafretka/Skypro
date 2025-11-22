from unittest.mock import patch
from src.transactions import read_transactions_csv, read_transactions_excel

@patch("pandas.read_csv")
def test_read_transactions_csv(mock_csv):
    expected = [{"a":"b"}]
    mock_csv.return_value.to_dict.return_value = expected
    result = read_transactions_csv("test_csv")
    assert result == expected


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_excel):
    expected = [{"a":"b"}]
    mock_excel.return_value.to_dict.return_value = expected
    result = read_transactions_excel("test_excel")
    assert result == expected