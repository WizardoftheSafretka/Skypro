import pytest
import json
import pathlib
from src.utils import get_list_dict_about_trans_json


def test_get_list_dict_about_trans_json_with_tmp(tmp_path: pathlib.Path):
    test_file = tmp_path / "test_file_json"
    data = [{"key": "value", "number": 123}, {"key": "value", "number": 1234}]
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    assert get_list_dict_about_trans_json(test_file) == data

def test_get_list_dict_about_trans_json_with_wrong_format(tmp_path: pathlib.Path):
    test_file = tmp_path / "test_file_json"
    data = []
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    assert get_list_dict_about_trans_json(test_file) == []
