def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функия, принимающая список словарей и возвращающая новый список словарей с ключем state"""

    return [oper_ for oper_ in operations if oper_.get("state") == state]


def sort_by_date(operations: list[dict], reverse_order: bool = True) -> list[dict]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""

    return sorted(operations, key=lambda x: x["date"], reverse=reverse_order)
