def get_mask_card_number(card_number: str) -> str:
    """Принять номер карты и вернуть его маску"""

    if card_number == "":
        return ""
    part_1 = card_number[:6]
    part_2 = "******"
    part_3 = card_number[-4:]

    mask_number = f"{part_1[:4]} {part_1[4:]}{part_2[:2]} {part_2[2:]} {part_3[:2]}{part_3[2:]}"

    return mask_number


def get_mask_account(account: int) -> str:
    """Принять номер счета и вернуть его маску"""


    return f"**{account[-4:]}"
