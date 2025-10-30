import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.fixture
def mask_card():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def mask_account():
    return "Счет 73654108430135874305"


def test_mask_card(mask_card):
    assert mask_account_card(mask_card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account(mask_account):
    assert mask_account_card(mask_account) == "Счет **4305"


@pytest.mark.parametrize("x, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                         ("Счет 64686473678894779589", "Счет **9589"),
                                         ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")])
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected