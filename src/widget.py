from masks import get_mask_account
from masks import get_mask_card_number
import re


def mask_account_card(type_card_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""

    type_card_number_list = type_card_number.split()
    new_list_alpha = []
    new_list_number = []
    result_number = ''
    for i in type_card_number_list:
        if i.isalpha():
            new_list_alpha.append(i)
        else:
            new_list_number.append(i)
    if 'Счет' in new_list_alpha:
        result_number += get_mask_account(''.join(new_list_number))
    else:
        result_number += get_mask_card_number(''.join(new_list_number))
    return f'{' '.join(new_list_alpha)} {result_number}'
