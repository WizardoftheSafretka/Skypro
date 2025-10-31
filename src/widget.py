from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""

    type_card_number_list = type_card_number.split()
    new_list_alpha = []
    new_list_number = []
    result_number = ""

    if len(type_card_number) == 0:
        return ""
    for i in type_card_number_list:
        if i.isalpha():
            new_list_alpha.append(i)
        else:
            new_list_number.append(i)
    if "Счет" in new_list_alpha:
        result_number += get_mask_account("".join(new_list_number))
    else:
        result_number += get_mask_card_number("".join(new_list_number))
    return f"{' '.join(new_list_alpha)} {result_number}"


def get_date(date_item: str) -> str:
    """Функция, которая возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    if len(date_item) == 0:
        return ""
    if "T" not in date_item and len(date_item) > 0:
        raise ValueError("Неверный формат даты")
    return f'{date_item[8:10]}.{date_item[5:7]}.{date_item[0:4]}'