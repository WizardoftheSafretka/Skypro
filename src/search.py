import re
from collections import Counter


def process_bank_search(operations_list: list[dict], keyword: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными
    о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка"""

    chosen_operations = []
    for operation in operations_list:
        description = operation.get("description", "")
        str_description = str(description)
        str_description.title()
        keyword.title()
        if isinstance(str_description, str) and re.search(keyword, str_description, flags=re.IGNORECASE):
            chosen_operations.append(operation)
    return chosen_operations


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях
    и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории"""

    categories_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        description_str = str(description)
        for cat in categories:
            if cat.lower() in description_str.lower():
                categories_counter[cat] += 1
    return categories_counter
