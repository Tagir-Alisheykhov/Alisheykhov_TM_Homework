import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def input_data_for_tests():
    """ Список входных данных для тестов 1 """
    values = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
              {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
              {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
    return values


@pytest.mark.parametrize("state, expected",
                         [("CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                          ("EXECUTED", [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}])])
def test_filter_by_state(input_data_for_tests, state, expected):
    """ Фильтрация словарей по заданному статусу 'state' """
    assert filter_by_state(input_data_for_tests, state) == expected


def test_filter_by_state_default_status(input_data_for_tests):
    """ Фильтрация словарей без заданного статуса 'state' (по умолчанию) """
    assert filter_by_state(input_data_for_tests) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


def test_sort_by_date(input_data_for_tests):
    """ Сортировка списка по умолчанию (по убыванию) """
    assert (sort_by_date(input_data_for_tests) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])


def test_sort_by_date_ascending(input_data_for_tests):
    """ Сортировка списка по возрастанию """
    assert (sort_by_date(input_data_for_tests, False) ==
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])


def test_sort_by_date_invalid_keys_and_invalid_date():
    """ Ошибка при отсутствии обязательного ключа """
    with pytest.raises(ValueError):
        sort_by_date([{"NOT_KEY": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}])
        sort_by_date([{"id": 41428829, "NOT_KEY": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}])
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "NOT_KEY": "2019-07-03T18:35:29.512364"}])
        sort_by_date([{"NOT_KEY": 41428829, "OT_KEY": "EXECUTED", "NOT_KY": "2019-07-03T18:35:29.512364"}])
        sort_by_date([{"NOT_KEY": 41428829, "OT_KEY": "EXECUTED", "NOT_KY": ""}])

