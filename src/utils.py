import os
import json
from dotenv import load_dotenv
from src.external_api import currency_conversion

load_dotenv()
API_KEY = os.getenv('KEY_API')
file_json = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
             "Homework_Alisheykhov_TM/data/operations.json")


def processing_json_file(filename: str) -> list[dict]:
    """Открытие j-son файла с транзакциями"""
    with (open(filename, encoding="UTF-8") as transactions_file):
        transactions = json.load(transactions_file)
        currency_current_transact = ""
        if transactions == "":
            raise ValueError("Передан пустой файл")
        for transact in transactions:
            if ('id' not in transact and 'state' not in transact
                    and 'operationAmount' not in transact and 'description' not in transact):
                continue
            else:
                if ('id' not in transact or 'state' not in transact
                        or 'operationAmount' not in transact or 'description' not in transact):
                    raise KeyError("Отсутствует обязательный ключ в транзакции")
                else:
                    if (len(str(transact['operationAmount']['currency']['code'])) != 3
                            or not isinstance(transact['operationAmount']['currency']['code'], str)):
                        raise ValueError("Неверный трехзначный код валюты в транзакции")
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


if __name__ == '__main__':
    data_file = processing_json_file(file_json)
    sum_all_transacts = sum_transactions(data_file)
    print(sum_all_transacts)
