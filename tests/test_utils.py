import pytest
from unittest.mock import patch, mock_open
from src.utils import get_list_dict_about_trans_json


@patch("builtins.open", new_callable=mock_open())
@patch("json.load")
def test_get_list_dict_about_trans_json(mock_load, new_callable):
        mock_load.return_value = {"key": "value"}
        result = get_list_dict_about_trans_json("test_data")
        expected = {"key": "value"}
        assert result == expected

def test_get_list_dict_about_trans_json_with_empty():
    assert get_list_dict_about_trans_json("") == []

