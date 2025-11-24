import json
import logging
from pathlib import Path
from typing import Any

Path("logs").mkdir(exist_ok=True)
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(massage)s", datefmt="%y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
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
