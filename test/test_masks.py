import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

@pytest.fixture
def card_numbers_normal():
    return "7000792289606361"


@pytest.fixture
def card_numbers_unnormal_min():
    return "7000792280"


@pytest.fixture
def card_numbers_unnormal_max():
    return "7000792280345345435"

@pytest.fixture
def card_numbers_zero():
    return ""

@pytest.fixture
def get_mask_account_normal():
    return "73654108430135874305"


@pytest.fixture
def get_mask_account_unnormal():
    return "736541084301358743053452622524"


@pytest.fixture
def get_mask_account_min():
    return "7365410"


def test_get_mask_card_number_normal(card_numbers_normal):
    assert get_mask_card_number(card_numbers_normal) == "7000 79** **** 6361"


def test_card_numbers_unnormal_min(card_numbers_unnormal_min):
        assert get_mask_card_number(card_numbers_unnormal_min) == "7000 79** **** 2280"


def test_get_card_numbers_unnormal_max(card_numbers_unnormal_max):
    assert get_mask_card_number(card_numbers_unnormal_max) == "7000 79** **** 5435"


def test_get_card_numbers_zero(card_numbers_zero):
    assert get_mask_card_number(card_numbers_zero) == ""


def test_get_mask_account_normal(get_mask_account_normal):
    assert get_mask_account(get_mask_account_normal) == "**4305"


def test_get_mask_account_unnormal(get_mask_account_unnormal):
    assert get_mask_account(get_mask_account_unnormal) == "**2524"


def test_get_mask_account_min(get_mask_account_min):
    assert get_mask_account(get_mask_account_min) == "**5410"

import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

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

@pytest.fixture
def get_mask_account_normal():
    return 73654108430135874305


@pytest.fixture
def get_mask_account_unnormal():
    return 736541084301358743053452622524


@pytest.fixture
def get_mask_account_min():
    return 7365410


def test_get_mask_card_number_normal(card_numbers_normal):
    assert get_mask_card_number(card_numbers_normal) == "7000 79** **** 6361"


def test_card_numbers_unnormal_min(card_numbers_unnormal_min):
        assert get_mask_card_number(card_numbers_unnormal_min) == "7000 79** **** 2280"


def test_get_card_numbers_unnormal_max(card_numbers_unnormal_max):
    assert get_mask_card_number(card_numbers_unnormal_max) == "7000 79** **** 5435"


def test_get_card_numbers_zero(card_numbers_zero):
    assert get_mask_card_number(card_numbers_zero) == ""


def test_get_mask_account_normal(get_mask_account_normal):
    assert get_mask_account(get_mask_account_normal) == "**4305"


def test_get_mask_account_unnormal(get_mask_account_unnormal):
    assert get_mask_account(get_mask_account_unnormal) == "**2524"


def test_get_mask_account_min(get_mask_account_min):
    assert get_mask_account(get_mask_account_min) == "**5410"

