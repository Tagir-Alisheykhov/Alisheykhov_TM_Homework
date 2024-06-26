"""
Функции для маскировки карты и счета клиента

Пример работы функции - 1, возвращающей маску карты
7000792289606361 -- входной аргумент
7000 79** **** 6361 -- выход функции

Пример работы функции - 2, возвращающей маску счета
73654108430135874305 -- входной аргумент
**4305 -- выход функции
"""


def get_mask_card_number(cart_numb: str) -> str:
    """Возвращает номер карты с маской"""
    new_list = list()
    new_list.append(cart_numb[0:4])
    new_list.append(cart_numb[4:6] + "**")
    new_list.append("****")
    new_list.append(cart_numb[12:])
    return " ".join(new_list)


def get_mask_account(account_number: str) -> str:
    """Возвращает номер счета с маской"""
    new_list = list()
    new_list.append("**" + account_number[-4:])
    return " ".join(new_list)


# Входные данные и их вывод для теста функций
# client_account_number = 73654108430135874305
# client_cart_number = 7000791119606361
# print(get_mask_account(str(client_account_number)))
# print(get_mask_card_number(str(client_cart_number)))
