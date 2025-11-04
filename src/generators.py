def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    while True:
        yield (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency)