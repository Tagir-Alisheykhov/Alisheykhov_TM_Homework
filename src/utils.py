import json
import requests

file_json = "C:/Users/Lenovo/practicalWork6/data4(homework).json"
# my_url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={received_currency}&amount={nominal}"


# headers2 = {
#     "apikey": "kP3oX8JfPcEPOOGTP6UJVjgnOTIPcyWo"
# }


def processing_json_file(filename) -> list[dict]:
    """Открытие j-son файла с транзакциями"""
    with open(filename, encoding="UTF-8") as transactions_file:
        transactions = json.load(transactions_file)
        return transactions


def sum_transactions(transactions_data: list[dict]) -> float:
    """Возвращает сумму всех транзакций в рублях"""
    list_amount = []
    received_currency = 'USD'
    nominal = 1
    to = 'RUB'
    finish_amount = 0
    for transact_dicts in transactions_data:
        if transact_dicts['operationAmount']['currency']['code'] == 'RUB':
            transactions_rub = transact_dicts['operationAmount']['amount']
            finish_amount += float(transactions_rub)
        else:
            # Необходимо поставить ошибку, если в транзакции отсутствует сумма или валюта
            currency_current_transact = transact_dicts['operationAmount']['currency']['code']
            amount_current_transact = float(transact_dicts['operationAmount']['amount'])
            list_amount.append(amount_current_transact)
            if currency_current_transact != received_currency:
                received_currency = currency_current_transact
    API_KEY = {
        "apikey": "CfWWBVZmMa73y0lNQiRLY9jjVH2tROBG"
    }
    my_url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={received_currency}&amount={nominal}"
    response = requests.get(my_url, headers=API_KEY)
    rate_one_currency = response.json()['result']
    for amount_current_transact in list_amount:
        finish_amount += amount_current_transact * rate_one_currency
    finish_result = round(finish_amount, 2)
    return finish_result
    # out = 201822128.19


if __name__ == '__main__':
    data_file = processing_json_file(file_json)
    sum_all_transact = sum_transactions(data_file)
    print(sum_all_transact)
