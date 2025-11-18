import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принять номер карты и вернуть его маску"""

    logger.info(f"Начало работы программы")
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        logger.error(f"Произошла ошибка: ValueError")
        raise ValueError("Неверный формат номера карты. Номер карты должен состоять из 16 цифр")
    else:
        logger.info(f"Конец работы программы. Маска номера карты создана")
        part_1 = str_card_number[:6]
        part_2 = "******"
        part_3 = str_card_number[-4:]
        mask_number = f"{part_1[:4]} {part_1[4:]}{part_2[:2]} {part_2[2:]} {part_3[:2]}{part_3[2:]}"
        return mask_number


def get_mask_account(account: str) -> str:
    """Принять номер счета и вернуть его маску"""

    logger.info(f"Начало работы программы")
    str_account = str(account)
    if len(str_account) != 20:
        logger.error(f"Произошла ошибка: ValueError")
        raise ValueError("Неверный формат номера счета. Номер счета должен состоять из 20 цифр")
    else:
        logger.info(f"Конец работы программы. Маска номера счета создана")
        return f"**{str_account[-4:]}"

if __name__ == "__main__":
    print(get_mask_card_number("1234567890874567"))
