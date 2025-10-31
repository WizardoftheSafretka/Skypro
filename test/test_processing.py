import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date

@pytest.fixture()
def filter_by_state_normal():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture()
def filter_by_state_without_state():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]



@pytest.mark.parametrize("x, y, expected", [(filter_by_state_normal, 'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                         (filter_by_state_normal, 'CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                                         (filter_by_state_without_state, 'CANCELED', [])])
def filter_by_state(x, y, expected):
    assert filter_by_state(x, y) == expected