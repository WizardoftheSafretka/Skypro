import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def transactions_currency():
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"name": "USD"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"name": "USD"}}},
        {"id": 3, "description": "Перевод со карты на карту", "operationAmount": {"currency": {"name": "руб."}}},
        {"id": 4, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"name": "руб."}}},
    ]


def test_filter_by_currency_usd(transactions_currency):
    expected_result = filter_by_currency(transactions_currency, "USD")
    assert (next(expected_result)) == {
        "id": 1,
        "description": "Перевод организации",
        "operationAmount": {"currency": {"name": "USD"}},
    }, {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"name": "USD"}}}


def test_filter_by_currency_rub(transactions_currency):
    expected_result = filter_by_currency(transactions_currency, "руб.")
    assert (next(expected_result)) == {
        "id": 3,
        "description": "Перевод со карты на карту",
        "operationAmount": {"currency": {"name": "руб."}},
    }, {"id": 4, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"name": "руб."}}}


def test_transaction_descriptions(transactions_currency):
    expected_result = transaction_descriptions(transactions_currency)
    assert (next(expected_result)) == "Перевод организации"
    assert (next(expected_result)) == "Перевод со счета на счет"
    assert (next(expected_result)) == "Перевод со карты на карту"
    assert (next(expected_result)) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "start, stop, first, second",
    [
        (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0002"),
        (99, 101, "0000 0000 0000 0099", "0000 0000 0000 0100"),
        (999, 1001, "0000 0000 0000 0999", "0000 0000 0000 1000"),
    ],
)
def test_card_number_generator(start, stop, first, second):
    gen = card_number_generator(start, stop)
    assert next(gen) == first
    assert next(gen) == second
