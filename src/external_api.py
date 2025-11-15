import os

import requests
from dotenv import load_dotenv


def conversation(transaction: dict) -> float | str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""

    if transaction["operationAmount"]["currency"]["name"] == "руб.":
        return float(transaction["operationAmount"]["amount"])
    else:
        load_dotenv()
        code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            return float(result["result"])
        else:
            return f"Запрос не был успешным. Возможная причина: {response.reason}"
