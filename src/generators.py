from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция, которая должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    for transaction in (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency):
        yield transaction

