import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.fixture
def mask_card():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def mask_account():
    return "Счет 73654108430135874305"


@pytest.fixture
def mask_account_card_zero():
    return ""

@pytest.fixture
def get_date_right():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def get_date_wrong():
    return "05.11.2025"

@pytest.fixture
def get_date_zero():
    return ""

def test_mask_card(mask_card):
    assert mask_account_card(mask_card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account(mask_account):
    assert mask_account_card(mask_account) == "Счет **4305"

def test_mask_account_zero(mask_account_card_zero):
        assert mask_account_card(mask_account_card_zero) == ""


@pytest.mark.parametrize("x, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                         ("Счет 64686473678894779589", "Счет **9589"),
                                         ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")])
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected


def test_get_date_right(get_date_right):
    assert get_date(get_date_right) == "11.03.2024"


def test_get_date_wrong():
    with pytest.raises(ValueError) as exc_info:
        get_date("05.11.2025")
    assert str(exc_info.value) == "Неверный формат даты"


def test_get_date_zero(get_date_zero):
    assert get_date(get_date_zero) == ""