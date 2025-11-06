from typing import Iterator

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Функция, которая должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""


    while True:
        yield (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency)

