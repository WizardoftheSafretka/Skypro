import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def empty_number():
    return

@pytest.fixture()
def wrong_number():
    return 295295918471984782197489217414215

def test_get_mask_card_number():
    assert get_mask_card_number(1234567890121234) == "1234 56** **** 1234"

def test_get_mask_card_number_wrong_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(wrong_number)
    assert str(exc_info.value) == "Неверный формат номера карты. Номер карты должен состоять из 16 цифр"

def test_get_mask_card_number_empty_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(empty_number)
    assert str(exc_info.value) == "Неверный формат номера карты. Номер карты должен состоять из 16 цифр"

def test_get_mask_account():
    assert get_mask_account(12345678901256785678) == "**5678"

def test_get_mask_account_wrong_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(wrong_number)
    assert str(exc_info.value) == "Неверный формат номера счета. Номер счета должен состоять из 20 цифр"

def test_get_mask_account_empty_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(empty_number)
    assert str(exc_info.value) == "Неверный формат номера счета. Номер счета должен состоять из 20 цифр"


