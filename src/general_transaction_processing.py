import json
import logging
import re
from os import path
from typing import Any

from src.processing import filter_by_state
from src.widget import get_data, mask_account_cart

path_to_file_js = path.join(path.dirname(path.dirname(__file__)), "data/operations.json")
path_to_file_csv = path.join(path.dirname(path.dirname(__file__)), "transactions(from-csv).json")
path_to_file_xlsx = path.join(path.dirname(path.dirname(__file__)), "transactions(from-xlsx).json")
path_to_logfile = path.join(path.dirname(path.dirname(__file__)), "logs/new_func.log")

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(path_to_logfile, mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def search_by_status() -> Any:
    """
    Начало работы программы, взаимодействие с пользователем - выбор файла для обработки,
    выбор статуса транзакций в файле для последующего взаимодействия с выбранными с транзакциями
    :return:
    Список словарей с выбранными по статусу транзакциями
    """
    filter_value = ''
    file_with_transacts = ''
    continue_cycle_1 = True
    continue_cycle_2 = True
    while continue_cycle_1:
        try:
            choice_file = input(
                'Программа: Привет! Добро пожаловать '
                'в программу работы\nс банковскими '
                'транзакциями.\nВыберите необходимый '
                'пункт меню:\n1. Получить информацию о '
                'транзакциях из JSON-файла\n2. Получить '
                'информацию о транзакциях из CSV-файла\n3. '
                'Получить информацию о транзакциях из '
                'XLSX-файла\n\nПользователь: '
            )
            pattern = re.compile(r'^[1-3]$')
            match = pattern.fullmatch(choice_file)
            if not match:
                continue
            elif match.group() == '1':
                file_with_transacts = path_to_file_js
                logger.info('\nПрограмма: Для обработки выбран JSON-файл.')
                continue_cycle_1 = False
            elif match.group() == '2':
                file_with_transacts = path_to_file_csv
                logger.info('\nПрограмма: Для обработки выбран CSV-файл.')
                continue_cycle_1 = False
            elif match.group() == '3':
                file_with_transacts = path_to_file_xlsx
                logger.info('\nПрограмма: Для обработки выбран XLSX-файл.')
                continue_cycle_1 = False
        except AttributeError:
            logger.warning('\nПрограмма: Неверный ввод. Пожалуйста, выберите цифру от 1 до 3\n')
    while continue_cycle_2:
        choice = input(
                '\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n'
                'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\nПользователь: '
        )
        if choice.upper() == 'EXECUTED' or choice.upper() == 'CANCELED' or choice.upper() == 'PENDING':
            filter_value = choice
            continue_cycle_2 = False
        else:
            logger.warning(f'\nПрограмма: Статус операции \'{choice}\' недоступен.')
    with open(file_with_transacts, encoding='utf-8') as f:
        processing_file = json.load(f)
    # Фильтрация списка по статусу через импортированную функцию
    logger.info(f'\nПрограмма: Операции отфильтрованы по статусу: \'{filter_value.upper()}\'')
    result = filter_by_state(processing_file, filter_value)
    return result


def quantity_and_categories(operations: list[dict], list_category_operations: list) -> dict[str, int]:
    """
    Принимает список транзакций и список категорий транзакций. Далее функция задает формат
    для вывода полученной информации в консоль, а также формирует словарь с ключами категорий
    транзакций и значения с количеством транзакций в каждой категории
    :return:
    Словарь с уникальными категориями транзакций и количеством транзакций в каждой категории
    """
    to = ''
    from_ = ''
    amount = ''
    descript = ''
    currency_code = ''
    count_transacts = 0
    date_current_transact = ''
    dict_with_categories = dict()
    try:
        for only_operation in operations:
            for key, value in only_operation.items():
                if only_operation['operationAmount']['amount']:
                    amount = only_operation['operationAmount']['amount']
                    currency = only_operation['operationAmount']['currency']['code']
                    currency_code = currency
                if key == 'date':
                    date_current_transact = get_data(value)
                if key == 'from':
                    from_ = mask_account_cart(value)
                if key == 'to':
                    to = mask_account_cart(value)
                if key == 'description':
                    descript = value
            if to == '':
                logger.debug(f'{date_current_transact} {descript}\n{from_}\n{amount} {currency_code}\n')
            else:
                logger.debug(f'{date_current_transact} {descript}\n{from_} -> {to}\n{amount} {currency_code}\n')
        unique_categories = set(list_category_operations)
        list_unique_categories = [value for value in unique_categories]
        for category in range(len(unique_categories)):
            key = list_unique_categories[category]
            dict_with_categories[key] = 0
        for num, category in enumerate(dict_with_categories):
            for value in list_category_operations:
                if value == category:
                    count_transacts = dict_with_categories[category] + 1
                    dict_with_categories[category] = count_transacts
        return dict_with_categories
    except Exception as error:
        logger.error(f'Возникла ошибка: {error}')
        return dict_with_categories
