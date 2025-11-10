from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция, которая должна возвращать итератор, который поочередно выдает транзакции c заданной валютой"""

    for transaction in (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency
    ):
        yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""

    for n in range(start, stop + 1):
        str_n = str(n)
        while len(str_n) < 16:
            str_n = "0" + str_n
        card_number = f"{str_n[:4]} {str_n[4:8]} {str_n[8:12]} {str_n[12:]}"
        yield card_number
