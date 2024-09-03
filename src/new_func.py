import json
from os import path
from src.processing import filter_by_state

# Используем Логеры для выводом в консоль
# 1 - ФУНКЦИЯ

path_to_file_js = path.join(path.dirname(path.dirname(__file__)), 'data/operations.json')
path_to_file_csv = path.join(path.dirname(path.dirname(__file__)), 'data/operations.json')
path_to_file_xlsx = path.join(path.dirname(path.dirname(__file__)), 'data/operations.json')


def search_filter(transacts_js, transacts_csv, transacts_xlsx):
    """
    """
    file_with_transacts = ''
    choice_file = input('Привет! Добро пожаловать в программу работы\nс банковскими транзакциями.\n'
                        'Выберите необходимый пункт меню:\n'
                        '1. Получить информацию о транзакциях из JSON-файла\n'
                        '2. Получить информацию о транзакциях из CSV-файла\n'
                        '3. По лучить информацию о транзакциях из XLSX-файла\n'
                        '\n'
                        'Пользователь: ')

    if choice_file == '1':
        file_with_transacts = transacts_js
        print('Для обработки выбран JSON-файл.')
    elif choice_file == '2':
        file_with_transacts = transacts_js
        print('Для обработки выбран CSV-файл.')
    elif choice_file == '2':
        file_with_transacts = transacts_js
        print('Для обработки выбран XLSX-файл.')

    value_for_filter = input('\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n'
                             'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n'
                             '\n'
                             'Пользователь: ').lower()

    print(file_with_transacts)
    print(type(file_with_transacts))

    # with open(file_with_transacts) as file:
    #     file_values = json.load(file)
    # with open(file_values, encoding='UTF-8') as file:
    #     result = file_values.read()
    #     print(result)
    #     print(type(result))

    # result = filter_by_state(file_values, value_for_filter)
    # return result

    # Вызываем функцию, которая преобразовывает под фильтр
    # filtering_the_data = filter_by_state(transacts_js)


if __name__ == '__main__':
    res = search_filter(path_to_file_js, path_to_file_csv, path_to_file_xlsx)
    print(res)
    # print(path_to_file)

# После фильтрации программа выводит следующие вопросы для уточнения
# выборки операций, необходимых пользователю, и выводит в консоль операции,
# соответствующие выборке пользователя:
# ----------------------------------------------------------
# ДАННЫЕ ВОПРОСЫ ПОМЕСТИТЬ В ОДНУ ФУНКЦИЮ
# Программа: Отсортировать операции по дате? Да/Нет
# Пользователь: да
#
# Программа: Отсортировать по возрастанию или по убыванию?
# Пользователь: по возрастанию/по убыванию
#
# Программа: Выводить только рублевые транзакции? Да/Нет
# Пользователь: да
#
# Программа: Отфильтровать список транзакций по определенному слову
# в описании? Да/Нет
# Пользователь: да/нет
#
# Программа: Распечатываю итоговый список транзакций...
# Программа
# Всего банковских операций в выборке: 4
#-------------------------------------------------------------
# 08.12.2019 Открытие вклада
# Счет **4321
# Сумма: 40542 руб.
#
# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
#
# 18.07.2018 Перевод организации
# Visa Platinum 7492 65** **** 7202 -> Счет **0034
# Сумма: 8390 руб.
#
# 03.06.2018 Перевод со счета на счет
# Счет **2935 -> Счет **4321
# Сумма: 8200 EUR