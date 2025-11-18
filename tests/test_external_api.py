import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import conversation


@pytest.fixture()
def transaction_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_conversation_rub(transaction_rub):
    assert conversation(transaction_rub) == 31957.58


transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


@patch("requests.get")
def test_conversation_usd(mock_get):
    load_dotenv()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 664694.82125}
    result = conversation(transaction_usd)
    assert result == 664694.82125
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
        f"{transaction_usd['operationAmount']['currency']['code']}"
        f"&amount={transaction_usd['operationAmount']['amount']}",
        headers={"apikey": os.getenv("API_KEY")},
    )


@patch("requests.get")
def test_conversation_usd_wrong(mock_get):
    load_dotenv()
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {"result": 664694.82125}
    result = conversation(transaction_usd)
    assert "Запрос не был успешным. Возможная причина:" in result
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
        f"{transaction_usd['operationAmount']['currency']['code']}"
        f"&amount={transaction_usd['operationAmount']['amount']}",
        headers={"apikey": os.getenv("API_KEY")},
    )
