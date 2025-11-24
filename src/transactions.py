import pandas as pd
from black.linegen import delimiter_split


def read_transactions_csv(filename: str) -> list[dict]:
    """Считывание файла csv"""

    read_csv = pd.read_csv(filename, delimiter = ";")
    return read_csv.to_dict(orient="records")


def read_transactions_excel(filename: str) -> list[dict]:
    """Считывание файла excel"""

    read_excel = pd.read_excel(filename)
    return read_excel.to_dict(orient="records")
