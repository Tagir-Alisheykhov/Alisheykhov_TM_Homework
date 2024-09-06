# Пример входных данных
from src.widget import get_data
from os import path
import json

test_dict_list = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689"
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441"
    },
]


# test_dict_list = [
#   {
#     "id": 441945886,
#     "state": "CANCELED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "CANCELED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     }
#   }
# ]


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    filtered_list_dict = []
    for dict_values in list_dict:
        for _value_ in dict_values.values():
            if _value_ == state.upper():
                filtered_list_dict.append(dict_values)
    return filtered_list_dict


def sort_by_date(list_dict: list[dict], is_sort_default: bool = True) -> list[dict]:
    """
    Сортирует список-словарей по датам (по умолчанию - убывание)
     В цикле мы обращаемся к импортируемому тесту [src/widget.py/get_data],
     для того, чтобы проверить корректность данных по ключу "date" и значительно сократить код
    """
    for _dict in list_dict:
        get_data(_dict["date"])
        if "id" not in _dict or "state" not in _dict or "date" not in _dict:
            raise ValueError(f"Отсутствие обязательного ключа:\n------> {_dict} <------")
    if is_sort_default:
        return sorted(list_dict, key=lambda dict_list: dict_list["date"], reverse=True)
    else:
        return sorted(list_dict, key=lambda dict_list: dict_list["date"])


# if __name__ == "__main__":
#     print(filter_by_state(test_dict_list, state="CANCELED"))
#     print(sort_by_date(test_dict_list))

