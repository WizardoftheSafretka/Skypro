import pandas as pd


def read_transactions_csv(filename: str) -> list[dict]:
    """Считывание файла csv"""

    read_csv = pd.read_csv(filename, delimiter=";")
    return read_csv.to_dict(orient="records")


def read_transactions_excel(filename: str) -> list[dict]:
    """Считывание файла excel"""

    read_excel = pd.read_excel(filename)
    return read_excel.to_dict(orient="records")


if __name__ == "__main__":
    print(read_transactions_excel("../data/transactions_excel.xlsx"))
