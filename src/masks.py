def get_mask_card_number(card_number: int) -> str:
    """Принять номер карты и вернуть его маску"""

    card_number_str = str(card_number)
    if str(card_number) == "":
        return ""
    part_1 = card_number_str[:6]
    part_2 = "******"
    part_3 = card_number_str[-4:]

    mask_number = f"{part_1[:4]} {part_1[4:]}{part_2[:2]} {part_2[2:]} {part_3[:2]}{part_3[2:]}"

    return mask_number


def get_mask_account(account: int) -> str:
    """Принять номер счета и вернуть его маску"""

    mask_account_str = str(account)

    return f"**{mask_account_str[-4:]}"

if __name__ == "__main__":
    print(get_mask_card_number(''))