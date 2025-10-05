def get_mask_card_number(card_number: str) -> str:
    """Принять номер карты и вернуть его маску"""

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Принять номер счета и вернуть его маску"""

    return f"**{account[-4:]}"
