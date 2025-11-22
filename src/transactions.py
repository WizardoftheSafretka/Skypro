from typing import Any, Hashable

import pandas as pd


def read_transactions_csv(filename: str) -> dict[Hashable, Any]:
    """Считывание файла csv"""

    read_csv = pd.read_csv(filename)
    return read_csv.to_dict()


def read_transactions_excel(filename: str) -> list[dict]:
    """Считывание файла excel"""

    read_excel = pd.read_excel(filename)
    return read_excel.to_dict(orient="records")
