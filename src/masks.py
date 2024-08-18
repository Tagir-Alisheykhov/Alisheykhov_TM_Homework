"""
Функции для маскировки карты и счета клиента

Пример работы функции - 1, возвращающей маску карты
7000792289606361 -- входной аргумент
7000 79** **** 6361 -- выход функции

Пример работы функции - 2, возвращающей маску счета
73654108430135874305 -- входной аргумент
**4305 -- выход функции
"""

import logging
from os import path
from typing import Any

path_to_logs = path.join(path.dirname(path.dirname(__file__)), "logs/masks.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    filename=path_to_logs,
    filemode="w",
    encoding="UTF-8",
)
logger = logging.getLogger(__name__)

logger.info("Запуск программы маскировки номера карты и счёта")


def get_mask_card_number(cart_numb: str | int) -> Any:
    """Возвращает номер карты с маской"""
    try:
        logger.info("Запуск функции маскировки номера карты")
        cart_numb_str = str(cart_numb)
        logger.info("Проверка корректности номера карты")
        if cart_numb == "":
            raise ValueError("Нет данных")
        if not cart_numb_str.isdigit():
            raise ValueError("Номер должен состоять только из цифр")
        if len(cart_numb_str) != 16:
            raise ValueError("Неверный номер карты")
        new_list = list()
        logger.info("Номер карты корректный")
        logger.info("Процесс преобразования номера карты")
        new_list.append(cart_numb_str[0:4])
        new_list.append(cart_numb_str[4:6] + "**")
        new_list.append("****")
        new_list.append(cart_numb_str[12:])
        logger.info("Завершение функции маскировки номера карты")
        return " ".join(new_list)
    except Exception as err:
        logger.error(f"Произошла ошибка: {err}")


def get_mask_account(account_number: str) -> Any:
    """Возвращает номер счета с маской"""
    try:
        logger.info("Запуск функции маскировки номера счёта")
        account_number_str = str(account_number)
        logger.info("Проверка корректности номера счёта")
        if account_number == "":
            raise ValueError("Нет данных")
        if not account_number_str.isdigit():
            raise ValueError("Номер должен состоять только из цифр")
        if len(account_number_str) != 20:
            raise ValueError("Неверный номер счета")
        logger.info("Процесс преобразования номера счёта")
        new_list = list()
        new_list.append("**" + account_number_str[-4:])
        logger.info("Завершение функции маскировки номера счёта")
        return " ".join(new_list)
    except Exception as err:
        logger.error(f"Произошла ошибка: {err}")


# Входные данные и их вывод для теста функций
if __name__ == "__main__":
    client_cart_number = 7000791119606365
    client_account_number = "73654108430135874305"
    print(get_mask_card_number(str(client_cart_number)))
    print(get_mask_account(str(client_account_number)))
