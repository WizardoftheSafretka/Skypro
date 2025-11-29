import pytest

from src.search import process_bank_operations, process_bank_search


@pytest.fixture()
def operations():
    result = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    return result


def test_process_bank_search(operations):
    result = process_bank_search(operations, "открытие")
    expected = [{"description": "Открытие вклада"}]
    assert result == expected


def test_process_bank_operations(operations):
    assert process_bank_operations(operations, ["Перевод организации"]) == {"Перевод организации": 2}
