import os
import json
from dotenv import load_dotenv
from src.external_api import currency_conversion

load_dotenv()
API_KEY = os.getenv('KEY_API')
file_json = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
             "Homework_Alisheykhov_TM/data/operations.json")


def processing_json_file(filename) -> list[dict]:
    """Открытие j-son файла с транзакциями"""
    with open(filename, encoding="UTF-8") as transactions_file:
        transactions = json.load(transactions_file)
        try:
            if transactions == [None]:
                raise ValueError("Файл c транзакциями пуст")
            for transact in transactions:
                empty_transact = 0
                currency_current_transact = transact['operationAmount']['currency']['code']
                if transact == {}:
                    print(f"Найдена пустая транзакция. Количество: {empty_transact}")
                    continue
                elif len(str(currency_current_transact)) != 3 and not isinstance(currency_current_transact, str):
                    raise ValueError("Неверный трехзначный код валюты")
                elif 'id' not in transact or 'state' not in transact or 'operationAmount' not in transact:
                    raise ValueError("Отсутствует обязательный ключ")
                elif 'amount' not in transact or 'currency' not in transact:
                    raise ValueError("Отсутствует обязательный под-ключ ключа 'operationAmount'")
                elif 'name' not in transact or 'code' not in transact:
                    raise ValueError("Отсутствует обязательный под-ключ ключа 'currency'")
        except ValueError as error:
            print(f"'ERROR': {error}")
        return transactions


def sum_transactions(transactions_data: list[dict]) -> float:
    """Возвращает сумму всех транзакций в рублях"""
    list_currency = []
    list_amount = []
    finish_amount = 0
    received_currency = 'USD'
    for transact_dicts in transactions_data:
        currency_current_transact = transact_dicts['operationAmount']['currency']['code']
        amount_current_transact = float(transact_dicts['operationAmount']['amount'])
        if currency_current_transact == 'RUB':
            finish_amount += amount_current_transact
        else:
            list_amount.append(amount_current_transact)
            list_currency.append(currency_current_transact)
            for current_currency in list_currency:
                if current_currency != received_currency:
                    received_currency = current_currency
                else:
                    continue
    conversion = currency_conversion(received_currency)
    for amount_one_transact in list_amount:
        finish_amount += (conversion * amount_one_transact)

    return round(finish_amount, 2)
# 2627938.96 - only rubles
# 203973571.68 - all transacts


if __name__ == '__main__':
    data_file = processing_json_file(file_json)
    sum_all_transacts = sum_transactions(data_file)
    print(sum_all_transacts)
