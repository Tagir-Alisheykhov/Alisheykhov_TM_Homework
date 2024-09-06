import json
from os import path
import logging
import re
from src.processing import filter_by_state
from src.widget import get_data, mask_account_cart

path_to_file_js = path.join(path.dirname(path.dirname(__file__)), 'data/operations.json')
path_to_file_csv = path.join(path.dirname(path.dirname(__file__)), 'transactions(from-csv).json')
path_to_file_xlsx = path.join(path.dirname(path.dirname(__file__)), 'transactions(from-xlsx).json')

path_to_logfile = path.join(path.dirname(path.dirname(__file__)), 'logs/new_file.log')


# -------------------------------------------------------------->>>
# ВРЕМЕННЫЙ СЧЕТЧИК - ДЛЯ ПОДСЧЕТА НАЧАЛЬНОГО КОЛИЧЕСТВА ТРАНЗАКЦИЙ
# ______________________________________________________________>>>
count = 0
with open(path_to_file_js, encoding='UTF-8') as file:
    file_values = json.load(file)
    for transact in file_values:
        if transact:
            count += 1
print(f'\nВСЕГО ТРАНЗАКЦИЙ В ФАЙЛЕ: [{count}]\n')
# --------------------------------------------------------------<<<

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    filename=path_to_logfile,
    filemode='w',
    encoding='UTF-8'
)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# ЛОГИ ЗАПИСЫВАЮТСЯ НЕ ТУДА, КУДА НУЖНО


def search_by_status():
    """
    """
    file_with_transacts = ''

    pattern = re.compile(r'\d')

    continue_cycle_1 = True
    while continue_cycle_1:
        choice_file = input('Привет! Добро пожаловать в программу работы\nс банковскими транзакциями.\n'
                            'Выберите необходимый пункт меню:\n'
                            '1. Получить информацию о транзакциях из JSON-файла\n'
                            '2. Получить информацию о транзакциях из CSV-файла\n'
                            '3. По лучить информацию о транзакциях из XLSX-файла\n'
                            '\n'
                            'Пользователь: ')

        match = pattern.fullmatch(choice_file)
        # ОБРАБОТАТЬ ОШИБКУ, ЕСЛИ НАПРИМЕР ВВЕСТИ ДВУХЗНАЧНОЕ ЧИСЛО
        # ОБРАБОТАТЬ ОШИБКУ, ЕСЛИ ТРАНЗАКЦИЯ ПУСТАЯ (src/utils.py/processing_json_file обрабатывает)
        if match.group() == '1':
            file_with_transacts = path_to_file_js
            logger.info('Программа: Для обработки выбран JSON-файл.')
            continue_cycle_1 = False
        elif match.group() == '2':
            file_with_transacts = path_to_file_csv
            logger.info('Программа: Для обработки выбран CSV-файл.')
            continue_cycle_1 = False
        elif match.group() == '3':
            file_with_transacts = path_to_file_xlsx
            logger.info('Программа: Для обработки выбран XLSX-файл.')
            continue_cycle_1 = False
        else:
            logger.warning('\nПрограмма: Введите правильный порядковый номер файла от 1 до 3\n')
    filter_value = ''
    continue_cycle_2 = True
    while continue_cycle_2:
        choice = str(input('\nПользователь: Введите статус, по которому необходимо выполнить фильтрацию.\n'
                           'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\nПользователь: '))
        if choice.upper() == 'EXECUTED' or choice.upper() == 'CANCELED' or choice.upper() == 'PENDING':
            filter_value = choice
            continue_cycle_2 = False
        else:
            logger.warning(f"Статус операции '{choice}' недоступен.")
    with open(file_with_transacts, encoding='UTF-8') as f:
        processing_file = json.load(f)

    # Фильтрация списка по статусу через импортированную функцию
    logger.info(f'Программа: Операции отфильтрованы по статусу: {filter_value.upper()}')

    result = filter_by_state(processing_file, filter_value)
    return result


#  КАТЕГОРИИ ТО ДОЛЖНЫ БЫТЬ СВЕЖИМИ
def quantity_and_categories(filtered_operations, list_category_operations):
    """
    Принимает список транзакций и список категорий транзакций
    """
    # Блок переменных для блока вывода транзакций
    descript = ''
    from_ = ''
    to = ''
    amount = ''
    currency_code = ''
    date_current_transact = ''

    # Вывод данных отфильтрованных транзакций в консоль
    for only_operation in filtered_operations:
        for key, value in only_operation.items():
            if key == 'date':
                date_current_transact = get_data(value)
            if key == 'description':
                descript = value
            if key == 'from':
                from_ = mask_account_cart(value)
            if key == 'to':
                to = mask_account_cart(value)
            if transact['operationAmount']['amount']:
                amount = transact['operationAmount']['amount']
                currency = transact['operationAmount']['currency']['code']
                currency_code = currency
        if to == '':
            logger.info(f'{date_current_transact} {descript}\n{from_}\n{amount} {currency_code}\n')
        else:
            logger.info(f'{date_current_transact} {descript}\n{from_} -> {to}\n{amount} {currency_code}\n')

    # Данный блок преобразовывает список названий транзакций в словарь с количеством транзакций
    unique_categories = set(list_category_operations)
    list_unique_categories = [value for value in unique_categories]
    new_dict = dict()

    for category in range(len(unique_categories)):
        key = list_unique_categories[category]
        new_dict[key] = 0

    count_ = 0
    for num, category in enumerate(new_dict):
        for value in list_category_operations:
            if value == category:
                count_ = new_dict[category] + 1
                new_dict[category] = count_

    # ЗДЕСЬ ДОЛЖНО ПРОВОДИТЬСЯ СУММИРОВАНИЕ КОЛ-ВА ТРАНЗ-Й ИЗ КРАЙНЕГО БЛОКА
    counter = 0
    for category in new_dict:
        c = new_dict[category]
        counter += int(c)
    logger.info(f"общее количество категорий из последнего блока второй функции {counter}")

    return new_dict

# ЗАВТРА
# решить проблему с декодированием файлов (в функции которая отвечает за запись файла) (типо решено)
# Добавить Loggers (нужно создать общий файл с логами для main.py и для src/new_func.py)
# Добавить регулярные выражения
# Добавить аннотацию
# Обработать ошибку, если в списке пустая транзакция (вроде это можно найти в первой функции src/utils.py)
# Чекнуть ошибку во второй функции где преобразование в словарь (возможно нужно поменять класс на LIST)
