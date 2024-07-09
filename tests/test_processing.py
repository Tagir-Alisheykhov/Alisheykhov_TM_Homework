import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def input_data_for_tests():
    values = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
              {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
              {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
    return values


@pytest.mark.parametrize("state, expected",
                         [("CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])])
def test_filter_by_state(input_data_for_tests, state, expected):
    assert filter_by_state(input_data_for_tests, state) == expected


def test_sort_by_date(input_data_for_tests):
    assert (sort_by_date(input_data_for_tests) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])

