def get_mask_card_number(card_number: int) -> str:
    """Принять номер карты и вернуть его маску"""

    str_card_number = str(card_number)
    return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account: int) -> str:
    """Принять номер счета и вернуть его маску"""

    str_account = str(account)
    return f"**{str_account[-4:]}"
