import pytest

from src.widget import get_date, mask_account_card


def test_mask_card():
    assert mask_account_card("Visa Electron 1234567890121234") == "Visa Electron 1234 56** **** 1234"

def test_mask_account():
    assert mask_account_card("Счет 12345678901212341234") == "Счет **1234"

def test_mask_card_wrong_number():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Visa 123")
    assert str(exc_info.value) == "Неверный формат номера карты. Номер карты должен состоять из 16 цифр"

def test_get_mask_card_number_empty_number():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Visa")
    assert str(exc_info.value) == "Неверный формат номера карты. Номер карты должен состоять из 16 цифр"

def test_get_mask_account_wrong_number():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 123")
    assert str(exc_info.value) == "Неверный формат номера счета. Номер счета должен состоять из 20 цифр"

def test_get_mask_account_empty_number():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 123")
    assert str(exc_info.value) == "Неверный формат номера счета. Номер счета должен состоять из 20 цифр"

def test_get_date_right():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

def test_get_date_wrong():
    with pytest.raises(ValueError) as exc_info:
        get_date("22.22.22")
    assert str(exc_info.value) == "Неверный формат даты"

def test_get_date_empty():
    with pytest.raises(ValueError) as exc_info:
        get_date("")
    assert str(exc_info.value) == "Неверный формат даты"