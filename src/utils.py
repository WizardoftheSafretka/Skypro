import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_dict_about_trans_json(file_name: str) -> Any:
    """Функция, возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    logger.info("Начало работы программы")
    try:
        with open(file_name, encoding="utf-8") as f:
            data = json.load(f)
        result = data
        logger.info("Данные загружены")
        return result
    except Exception as ex:
        logger.error(f"Данные невозможно загрузить. Тип ошибки: {ex}")
        print("Нет возможности открыть файл")
        return []
