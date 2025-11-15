import json
from typing import Any


def get_list_dict_about_trans_json(file_name: str) -> Any:
    """Функция, возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    try:
        with open(file_name, encoding="utf-8") as f:
            data = json.load(f)
        result = data
        return result
    except FileNotFoundError:
        print("Нет возможности открыть файл")
        return []
