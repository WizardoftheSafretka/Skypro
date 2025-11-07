from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция, которая должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    for transaction in (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency):
        yield transaction


def transaction_descriptions(transactions: list) -> iter:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        if 'description' in transaction:
            yield transaction['description']