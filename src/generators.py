from typing import Iterator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transacts: list[dict], currency: str = "USD") -> Iterator[dict[str | str, int, dict]]:
    """
    Функция-генератор. Поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    for _dict in transacts:
        if (
            "operationAmount" not in _dict
            or "currency" not in _dict["operationAmount"]
            or "name" not in _dict["operationAmount"]["currency"]
            or "code" not in _dict["operationAmount"]["currency"]
        ):
            raise KeyError("Ключ не найден")
        transacts_current_code = _dict["operationAmount"]["currency"]["code"]
        if transacts_current_code == currency:
            yield _dict


def transaction_descriptions(transact: list[dict]) -> Iterator[str]:
    """Генератор возвращает описание каждой операции по очереди"""
    for _dict in transact:
        if "description" in _dict:
            way_to_the_key = _dict["description"]
            yield way_to_the_key
        else:
            raise KeyError("Ключ не найден")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор выдает номера банковских карт в определенном формате.
    Генератор может сгенерировать номера карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    start_inx = start
    cart_inx = 1
    while start_inx <= end:
        generated_numb = str(start_inx)
        while len(generated_numb) < 16:
            generated_numb = "0" + generated_numb
        new_list = list()
        new_list.append(list(generated_numb[:4]))
        new_list.append(list(generated_numb[4:8]))
        new_list.append(list(generated_numb[8:12]))
        new_list.append(list(generated_numb[12:]))
        filtered_numb = ["".join(i) for i in new_list]
        result = " ".join(filtered_numb)
        yield result
        cart_inx += 1
        start_inx += 1


if __name__ == "__main__":
    # -------- ГЕНЕРАТОР-1 filter_by_currency --------
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(5):
            print(next(usd_transactions))
    except StopIteration:
        print(f"> Вызываемый генератор '{filter_by_currency}'- пуст <\n")

    # -------- ГЕНЕРАТОР-2 transaction_descriptions --------
    descriptions = transaction_descriptions(transactions)
    try:
        for _ in range(6):
            print(next(descriptions))
    except StopIteration:
        print(f"> Вызываемый генератор '{transaction_descriptions}'- пуст <\n")

    # -------- ГЕНЕРАТОР-3 card_number_generator --------
    for cart_number in card_number_generator(9999999999999995, 9999999999999999):
        print(cart_number)