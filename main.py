import logging
import re
from os import makedirs, path

from src.general_transaction_processing import quantity_and_categories, search_by_status
from src.processing import sort_by_date

path_to_logfile = path.join(path.dirname(path.dirname(__file__)), "logs/")
log_file_path = path.join(path_to_logfile, "main.log")

makedirs(path_to_logfile, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file_path, mode="a+", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def main() -> dict:
    """
    Объединяет функционал модуля 'general_transaction_processing'
    для обработки транзакций, взаимодействия с пользователем
    :return:
    Выводит словарь, где ключи - названия всех категорий транзакций
    из обрабатываемого файла, а значения - количество транзакций в каждой категории
    """
    # -------------------------------------------------------------------------------------------------------------
    direction = True                                    # Переменная для сортировки по возрастанию/убыванию
    list_category = []                                  # Список "descriptions"
    sum_all_operations = 0                              # Сумма всех банковских операций (отфильтрованных)
    filtered_currency = []                              # Список с отфильтрованными транзакциями (после 3-го вопроса)
    sorted_date_in_transacts = []                       # Отсортированные транзакции по дате (после 1-2 вопросов)
    finish_filtered_currency = []                       # Список с отфильтрованными транзакциями (после 4-го вопроса)
    search_transacts_by_string = search_by_status()     # Фильтр транзакций по статусу (ключу) 'state'
    # -------------------------------------------------------------------------------------------------------------
    try:
        # Первый и второй вопросы (сортировка по дате, возрастанию/убыванию)
        question_1 = str(input('\nПрограмма: Отсортировать операции по дате? Да/Нет\n\nПользователь: '))
        if question_1.lower() == 'да':
            question_2 = str(input("\nПрограмма: Отсортировать по возрастанию или по убыванию?\n\nПользователь: "))
            if 'возрастанию' in question_2.lower() or 'да' in question_2.lower():
                direction = False
                sorted_date_in_transacts = sort_by_date(search_transacts_by_string, direction)
            else:
                sorted_date_in_transacts = search_transacts_by_string
        else:
            sorted_date_in_transacts = search_transacts_by_string
    except Exception as err_1:
        logger.error(f'При обработке вопросов возникла ошибка {err_1}')
    try:
        # Третий вопрос (выбор валюты)
        question_3 = str(input('\nПрограмма: Выводить только рублевые транзакции?\n\nПользователь: '))
        if 'да' in question_3.lower():
            for transact in list(sorted_date_in_transacts):
                if transact['operationAmount']['currency']['code'] == 'RUB':
                    filtered_currency.append(transact)
        else:
            for transact in list(sorted_date_in_transacts):
                filtered_currency.append(transact)
    except Exception as err_2:
        logger.error(f'При обработке вопроса возникла ошибка {err_2}')
    try:
        # Четвертый вопрос (транзакция по ключевому слову)
        question_4 = str(
            input("\nОтфильтровать список транзакций по определенному слову в " "описании? Да/Нет\n\nПользователь: ")
        )
        if question_4.lower() == "да":
            sub_question = str(input("\nВведите слово/фразу:\n").lower())
            for transact in filtered_currency:
                pattern = re.search(sub_question, transact["description"].lower())
                if pattern:
                    finish_filtered_currency.append(transact)
                    list_category.append(transact["description"])
        else:
            for transact in filtered_currency:
                finish_filtered_currency.append(transact)
                list_category.append(transact["description"])
    except Exception as err_3:
        logger.error(f'При обработке вопроса возникла ошибка {err_3}')
    logger.info("\nПрограмма: Распечатываю итоговый список транзакций...")
    for only_one_operation in finish_filtered_currency:
        if only_one_operation:
            sum_all_operations += 1
    logger.info(f"\nПрограмма:\nВсего банковских операций в выборке: {sum_all_operations}\n")
    # Передаем данные в функцию 'quantity_and_categories' и возвращаем словарь
    # с количеством транзакций в каждой категории
    dict_of_categories_and_quantity = quantity_and_categories(finish_filtered_currency, list_category)
    return dict_of_categories_and_quantity


if __name__ == "__main__":
    print(main())
