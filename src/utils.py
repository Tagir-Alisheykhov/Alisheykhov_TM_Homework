import json
import logging
import os
from os import path
from typing import Any

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("KEY_API")
new_filename = "operations"
path_to_data = path.join(path.dirname(path.dirname(__file__)), "data/")
file_json = path.join(path.dirname(path.dirname(__file__)), "data/operations.json")
path_to_logs = path.join(path.dirname(path.dirname(__file__)), "logs/utils.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    filename=path_to_logs,
    filemode="w",
    encoding="UTF-8",
)
logger = logging.getLogger(__name__)
logger.info("Запуск программы конвертации валюты")


def processing_json_file(path_to_d: str) -> Any:
    """Чтение j-son файла с транзакциями"""
    logger.info("Проверка корректности входных данных")
    with open(path_to_d, encoding="UTF-8") as transactions_file:
        transactions = json.load(transactions_file)
        status_operation = False
        if transactions == "":
            raise ValueError("Передан пустой файл")
        for transact in transactions:
            if (
                "id" not in transact
                and "state" not in transact
                and "operationAmount" not in transact
                and "description" not in transact
            ):
                continue
            else:
                if (
                    "id" not in transact
                    or "state" not in transact
                    or "operationAmount" not in transact
                    or "description" not in transact
                ):
                    raise KeyError("Отсутствует обязательный ключ в транзакции")
                elif len(str(transact["operationAmount"]["currency"]["code"])) != 3 or not isinstance(
                    transact["operationAmount"]["currency"]["code"], str
                ):
                    raise ValueError("Неверный трехзначный код валюты в транзакции")
                else:
                    status_operation = True
        if status_operation:
            logger.info("Данные успешно прошли проверку")
    return transactions


def sum_transactions(transactions_data: list[dict[str, dict]]) -> Any:
    """Возвращает сумму всех транзакций в рублях"""
    try:
        logger.info("Запуск программы конвертации валюты")
        list_currency = []
        list_amount = []
        finish_amount = 0.0
        received_currency = "USD"
        # conversion = currency_conversion(received_currency)
        conversion = 85.77  # Курс валюты на случай запуска функции без интернета и т.п. (Необходимо раскомментировать)

        logger.info("Получение данных о валюте каждой отдельной транзакции")
        for transact_dicts in transactions_data:
            currency_current_transact = transact_dicts["operationAmount"]["currency"]["code"]
            amount_current_transact = float(transact_dicts["operationAmount"]["amount"])
            if currency_current_transact == "RUB":
                float(finish_amount) + amount_current_transact
            else:
                list_amount.append(amount_current_transact)
                list_currency.append(currency_current_transact)
                for current_currency in list_currency:
                    if current_currency != received_currency:
                        received_currency = current_currency
                    else:
                        continue
        logger.info("Получение актуальных данных о курсе иностранных валют")
        logger.info("Применяем конвертацию к сумме каждой транзакции с иностранной валютой")
        for amount_one_transact in list_amount:
            multiply = conversion * amount_one_transact
            finish_amount = finish_amount + multiply

        logger.info("Возвращаем сумму всех транзакций в рублях")
        logger.info("Конец работы приложения")
        return round(finish_amount, 2)
    except Exception as err:
        logger.error(f"Произошла ошибка: {err}", exc_info=True)


if __name__ == "__main__":
    data_file = processing_json_file(path_to_data, new_filename)
    print(sum_transactions(data_file))
