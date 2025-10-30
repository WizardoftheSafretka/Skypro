import pytest
from src.masks import get_mask_card_number

@pytest.fixture
def card_numbers_normal():
    return 7000792289606361


@pytest.fixture
def card_numbers_unnormal_min():
    return 7000792280


@pytest.fixture
def card_numbers_unnormal_max():
    return 7000792280345345435

@pytest.fixture
def card_numbers_zero():
    return ""


def test_get_mask_card_number_normal(card_numbers_normal):
    assert get_mask_card_number(card_numbers_normal) == "7000 79** **** 6361"


def test_card_numbers_unnormal_min(card_numbers_unnormal_min):
        assert get_mask_card_number(card_numbers_unnormal_min) == "7000 79** **** 2280"


def test_get_card_numbers_unnormal_max(card_numbers_unnormal_max):
    assert get_mask_card_number(card_numbers_unnormal_max) == "7000 79** **** 5435"


def test_get_card_numbers_zero(card_numbers_zero):
    assert get_mask_card_number(card_numbers_zero) == ""

