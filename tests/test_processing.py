import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2016-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2015-07-03T18:35:29.512364"},
    ]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2015-07-03T18:35:29.512364"}
    ]),
    ("CANCELED", [
        {"id": 2, "state": "CANCELED", "date": "2016-07-03T18:35:29.512364"},
    ])
])
def test_filter_by_state(state, expected, operations):
    result = filter_by_state(operations, state=state)
    assert result == expected

@pytest.mark.parametrize("reverse_order, expected", [
    (True, [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2016-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2015-07-03T18:35:29.512364"},
    ]),
    (False, [
        {"id": 3, "state": "EXECUTED", "date": "2015-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2016-07-03T18:35:29.512364"},
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ])
])
def test_sort_by_date(reverse_order, expected, operations):
    result = sort_by_date(operations, reverse_order=reverse_order)
    assert result == expected



