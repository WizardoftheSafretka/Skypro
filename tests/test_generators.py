import pytest
from src.generators import filter_by_currency

@pytest.fixture()
def transactions_currency():
    return [{"id": 1, "operationAmount": {"currency": {"name": "USD"}}},
            {"id": 2, "operationAmount": {"currency": {"name": "USD"}}},
            {"id": 3, "operationAmount": {"currency": {"name": "руб."}}},
            {"id": 4, "operationAmount": {"currency": {"name": "руб."}}},
            ]


def test_filter_by_currency_usd(transactions_currency):
    expected_result = filter_by_currency(transactions_currency, "USD")
    assert (next(expected_result)) == {'id': 1, 'operationAmount': {'currency': {'name': 'USD'}}}, {'id': 2, 'operationAmount': {'currency': {'name': 'USD'}}}

def test_filter_by_currency_rub(transactions_currency):
    expected_result = filter_by_currency(transactions_currency, "руб.")
    assert (next(expected_result)) == {"id": 3, "operationAmount": {"currency": {"name": "руб."}}}, {"id": 4, "operationAmount": {"currency": {"name": "руб."}}}