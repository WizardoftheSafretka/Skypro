def filter_by_state(list_dict:list[dict], state:str='EXECUTED') -> list[dict]:
    """Функия, принимающая список словарей и возвращающая новый список словарей с ключем state"""

    new_list = []
    for i in list_dict:
        if i.get("state") == state:
            new_list.append(i)

    return new_list
