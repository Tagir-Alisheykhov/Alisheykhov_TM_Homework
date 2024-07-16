transactions = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
                },
                {
          "id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
          "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод со счета на счет",
          "from": "Счет 19708645243227258542",
          "to": "Счет 75651667383060284188"
                }]


def filter_by_currency(transacts, currency="USD"):
    """
    Функция-генератор. Поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    for _dict in transacts:
        if ("operationAmount" not in _dict
            or "currency" not in _dict["operationAmount"]
                or "name" not in _dict["operationAmount"]["currency"]
               and "code" not in _dict["operationAmount"]["currency"]):
            raise KeyError("Ключ не найден")
        transacts_current_name = _dict["operationAmount"]["currency"]["name"]
        transacts_current_code = _dict["operationAmount"]["currency"]["code"]
        if transacts_current_name == currency and transacts_current_code == currency:
            yield _dict
        elif transacts_current_code != transacts_current_name:
            raise ValueError("Несоответствие значений ключей 'name' и 'code'.\nИх значения должны быть одинаковыми")


def transaction_descriptions(transact):
    for _dict in transact:
        if "description" not in _dict["description"]:
            raise KeyError("Ключ не найден")
        way_to_the_key = _dict["description"]
        yield way_to_the_key


if __name__ == "__main__":

    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(0):
            print(next(usd_transactions))
    except StopIteration:
        print(f":----: Вызываемый генератор '{filter_by_currency}' пуст :----:")

    descriptions = transaction_descriptions(transactions)
    try:
        for _ in range(5):
            print(next(descriptions))
    except StopIteration:
        print(f":----: Вызываемый генератор '{transaction_descriptions}' пуст :----:")
