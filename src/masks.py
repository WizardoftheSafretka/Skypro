def get_mask_card_number(card_number: int) -> str:
    """Принять номер карты и вернуть его маску"""
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        raise ValueError("Неверный формат номера карты. Номер карты должен состоять из 16 цифр")
    else:
        part_1 = str_card_number[:6]
        part_2 = "******"
        part_3 = str_card_number[-4:]
        mask_number = f"{part_1[:4]} {part_1[4:]}{part_2[:2]} {part_2[2:]} {part_3[:2]}{part_3[2:]}"
        return mask_number



def get_mask_account(account: int) -> str:
    """Принять номер счета и вернуть его маску"""
    str_account = str(account)
    if len(str_account) != 20:
        raise ValueError("Неверный формат номера счета. Номер счета должен состоять из 20 цифр")
    else:
        return f"**{str_account[-4:]}"
if __name__ == "__main__":
    print(get_mask_card_number(123))