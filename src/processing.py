def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функия, принимающая список словарей и возвращающая новый список словарей с ключем state"""

    new_list = []
    for i in list_dict:
        if i.get("state") == state:
            new_list.append(i)

    return new_list


def sort_by_date(list_dict: list[dict], reverse_order: bool = True) -> list[dict]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""

    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse_order)
