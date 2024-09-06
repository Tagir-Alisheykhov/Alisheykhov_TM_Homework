from src.new_func import search_by_status, quantity_and_categories
from src.processing import sort_by_date
import re


def main():

    search_transacts_by_string = search_by_status()  # -- Фильтр транзакций по статусу (ключу) 'state'
    direction = True                                 # -- Переменная для сортировки по возрастанию/убыванию
    sorted_date_in_transacts = ''                    # -- Отсортированные транзакции по дате (после 1-2 вопросов)
    filtered_currency = []                           # -- Список с отфильтрованными транзакциями (после 3-го вопроса)
    finish_filtered_currency = []                    # -- Список с отфильтрованными транзакциями (после 4-го вопроса)
    list_category = []                               # -- Список "descriptions"

    # ------------------------------------------------------------->>>
    # ВРЕМЕННЫЙ СЧЕТЧИК - для подсчета принимаемых функцией транзакций
    # _____________________________________________________________>>>
    #
    # count_tr = 0
    # for transact in search_transacts_by_string:
    #     if transact:
    #         count_tr += 1
    # print(print(f'\nВСЕГО ТРАНЗАКЦИЙ В СТАТУСЕ: [{count_tr}]\n'))
    # --------------------------------------------------------------<<<

    # Первый вопрос и второй (сортировка по дате, возрастанию/убыванию)
    SCHETCHIK_1_and_2_TRUE = 0
    SCHETCHIK_1_and_2_FALSE = 0

    question_1 = str(input('\nОтсортировать операции по дате? Да/Нет\n'))
    if question_1.lower() == 'да':

        question_2 = str(input('\nОтсортировать по возрастанию или по убыванию?\n'))
        if 'возрастанию' in question_2.lower() or 'да' in question_2.lower():
            direction = False
            sorted_date_in_transacts = sort_by_date(search_transacts_by_string, direction)
    #     ВРЕМЕННЫЙ ЦИКЛ
            for i in sorted_date_in_transacts:
                if i:
                    SCHETCHIK_1_and_2_TRUE += 1
        else:
            sorted_date_in_transacts = search_transacts_by_string
            # ВРЕМЕННЫЙ ЦИКЛ
            for i in sorted_date_in_transacts:
                if i:
                    SCHETCHIK_1_and_2_FALSE += 1
    else:
        sorted_date_in_transacts = search_transacts_by_string
        # ВРЕМЕННЫЙ ЦИКЛ
        for i in sorted_date_in_transacts:
            if i:
                SCHETCHIK_1_and_2_FALSE += 1

    if SCHETCHIK_1_and_2_TRUE != 0:
        print(f"СЧЁТЧИК 1-2 (Отсортировать операции по дате): {SCHETCHIK_1_and_2_TRUE} TRUE")
    else:
        print(f"СЧЁТЧИК 1-2 (Отсортировать операции по дате): {SCHETCHIK_1_and_2_FALSE} FALSE")

    # Третий вопрос (выбор валюты)
    SCHETCHIK_3_TRUE = 0
    SCHETCHIK_3_FALSE = 0
    question_3 = str(input('\nВыводить только рублевые транзакции?\n'))
    if 'да' in question_3.lower():
        for transact in list(sorted_date_in_transacts):
            if transact['operationAmount']['currency']['code'] == 'RUB':
                filtered_currency.append(transact)
                SCHETCHIK_3_TRUE += 1
    else:
        for transact in list(sorted_date_in_transacts):
            filtered_currency.append(transact)
            if transact:
                SCHETCHIK_3_FALSE += 1
    if SCHETCHIK_3_TRUE != 0:
        print(f"СЧЁТЧИК 3 (Выводить только рублевые транзакции): {SCHETCHIK_3_TRUE} TRUE")
    else:
        print(f"СЧЁТЧИК 3 (Выводить только рублевые транзакции): {SCHETCHIK_3_FALSE} FALSE")

    # Четвертый вопрос (транзакция по ключевому слову)
    SCHETCHIK_4_TRUE = 0
    SCHETCHIK_4_FALSE = 0
    question_4 = str(input('\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n'))
    if question_4.lower() == 'да':
        sub_question = str(input('\nВведите слово/фразу:\n').lower())
        for transact in filtered_currency:
            pattern = re.search(sub_question, transact['description'].lower())
            if not pattern:
                continue
            else:
                finish_filtered_currency.append(transact)
                list_category.append(transact['description'])
                SCHETCHIK_4_TRUE += 1
    else:
        for transact in filtered_currency:
            finish_filtered_currency.append(transact)
            list_category.append(transact['description'])
            SCHETCHIK_4_FALSE += 1

    if SCHETCHIK_4_TRUE != 0:
        print(f"СЧЁТЧИК 4 (Отфильтровать список транзакций по определенному слову в описании?): {SCHETCHIK_4_TRUE} TRUE")
    else:
        print(f"СЧЁТЧИК 4 (Отфильтровать список транзакций по определенному слову в описании?): {SCHETCHIK_4_FALSE} FALSE")

    # Передаем данные во вторую функцию и возвращаем словарь с количеством разных транзакций
    dict_of_categories_and_quantity = quantity_and_categories(finish_filtered_currency, list_category)
    return dict_of_categories_and_quantity


if __name__ == '__main__':
    print(main())

    # Обработка ошибок

    # Посмотреть сколько транзакций изначально и сколько выводит каждый из статусов,
    # а после проверяем сумму этих статусов, чтобы они совпали с изначальным количеством

    # Сделать проверку в первой функции если нет вообще значений

    # # Генерируем список со значениями ключей "description" (категории транзакций)
    # for transact in search_transacts_by_string:
    #     categories = transact['description']
    #     list_category.append(categories)

# CHECKLIST

# 1 - status -> (1) YES -> (2) YES -> (3) YES -> (4) YES -> (5) Вводим слово "перевод"
# Проверяем в ручную кол-во транзакций и сверяем с счетчиками
# EXECUTED ()
# 1 file ()
# 2 file ()
# 3 file ()
# CANCELED ()
# 1 file ()
# 2 file ()
# 3 file ()
# PENDING ()
# 1 file ()
# 2 file ()
# 3 file ()

# 2 - EXECUTED -> (1) YES -> (2) YES -> (3) YES -> (4) YES -> (5) Вводим слово "ПЕРЕВОД"
# Проверяем в ручную кол-во транзакций и сверяем с счетчиками
# EXECUTED ()
# 1 file ()
# 2 file ()
# 3 file ()
# CANCELED ()
# 1 file ()
# 2 file ()
# 3 file ()
# PENDING ()
# 1 file ()
# 2 file ()
# 3 file ()

# 3 - EXECUTED -> (1)(2) NO -> (3) NO -> (4) NO -> (5) Вводим слово "перевод"
# Должно выйти 85 транзакций
# Проверяем в ручную кол-во транзакций и сверяем со счетчиками
# EXECUTED ()
# 1 file ()
# 2 file ()
# 3 file ()
# CANCELED ()
# 1 file ()
# 2 file ()
# 3 file ()
# PENDING ()
# 1 file ()
# 2 file ()
# 3 file ()

# 3 - EXECUTED -> (1)(2) NO -> (3) YES -> (4) YES -> (5) Вводим слово "перевод"
# Должно выйти 40 транзакций
# EXECUTED ()
# 1 file ()
# 2 file ()
# 3 file ()
# CANCELED ()
# 1 file ()
# 2 file ()
# 3 file ()
# PENDING ()
# 1 file ()
# 2 file ()
# 3 file ()

# 3 - EXECUTED -> (1)(2) NO -> (3) NO -> (4) YES -> (5) Вводим слово "перевод"
# Должно выйти количество в зависимости от совпадений ключевых слов
# EXECUTED ()
# 1 file ()
# 2 file ()
# 3 file ()
# CANCELED ()
# 1 file ()
# 2 file ()
# 3 file ()
# PENDING ()
# 1 file ()
# 2 file ()
# 3 file ()