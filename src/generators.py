from typing import Iterator

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    while True:
        yield (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency)

