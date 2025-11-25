import re
from collections import Counter


def process_bank_search(operations_list: list[dict], keyword: str) -> list[dict]:
    """Функция поиска операций по кючевому слову"""

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
    """Функция возврата словаря с подсчетом категорий"""

    categories_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        description_str = str(description)
        for cat in categories:
            if cat.lower() in description_str.lower():
                categories_counter[cat] += 1
    return categories_counter
