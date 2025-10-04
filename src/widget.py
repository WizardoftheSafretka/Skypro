from masks import get_mask_account
from masks import get_mask_card_number
import re


def mask_account_card(type_card_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""

    type_card_number_list = type_card_number.split()
    type = re.search('[a-zA-Z]', type_card_number)
    number = type_card_number_list[1]
    if type == 'Счет':
        return f'{type}: {get_mask_account(number)}'
    else:
        return f'{type}: {mask_account_card(number)}'


if __name__ == '__main__':
    print(mask_account_card('Maestro 1596837868705199'))
