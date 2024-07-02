# Пример входных данных
test_dict_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    filtered_list_dict = []
    for dict_values in list_dict:
        if state == "EXECUTED":
            for value in dict_values.values():
                if value == state:
                    filtered_list_dict.append(dict_values)
        elif state:
            for value in dict_values.values():
                if value == state:
                    filtered_list_dict.append(dict_values)
    return filtered_list_dict


def sort_by_date(list_dict: list[dict], sort_default: str = "decrease") -> list[dict]:
    """
    Сортирует список-словарей по датам (по умолчанию - убывание)
    """
    if sort_default == "decrease":
        return sorted(list_dict, key=lambda dict_list: dict_list["date"], reverse=True)
    elif sort_default == "increase":
        return sorted(list_dict, key=lambda dict_list: dict_list["date"])


if __name__ == "__main__":
    print(filter_by_state(test_dict_list))
    print(sort_by_date(test_dict_list))
