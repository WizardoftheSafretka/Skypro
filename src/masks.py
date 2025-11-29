import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принять номер карты и вернуть его маску"""

    logger.info("Начало работы программы")
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        logger.error("Произошла ошибка: ValueError")
        raise ValueError("Неверный формат номера карты. Номер карты должен состоять из 16 цифр")
    else:
        logger.info("Конец работы программы. Маска номера карты создана")
        part_1 = str_card_number[:6]
        part_2 = "******"
        part_3 = str_card_number[-4:]
        mask_number = f"{part_1[:4]} {part_1[4:]}{part_2[:2]} {part_2[2:]} {part_3[:2]}{part_3[2:]}"
        return mask_number


def get_mask_account(account: str) -> str:
    """Принять номер счета и вернуть его маску"""

    logger.info("Начало работы программы")
    str_account = str(account)
    if len(str_account) != 20:
        logger.error("Произошла ошибка: ValueError")
        raise ValueError("Неверный формат номера счета. Номер счета должен состоять из 20 цифр")
    else:
        logger.info("Конец работы программы. Маска номера счета создана")
        return f"**{str_account[-4:]}"
