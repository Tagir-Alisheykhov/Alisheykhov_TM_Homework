"""
Функции для маскировки карты и счета клиента

Пример работы функции - 1, возвращающей маску карты
7000792289606361 -- входной аргумент
7000 79** **** 6361 -- выход функции

Пример работы функции - 2, возвращающей маску счета
73654108430135874305 -- входной аргумент
**4305 -- выход функции
"""


def get_mask_card_number(cart_numb: str | int) -> str:
    """Возвращает номер карты с маской"""
    cart_numb_str = str(cart_numb)
    if cart_numb == "":
        raise ValueError("Нет данных")
    if not cart_numb_str.isdigit():
        raise ValueError("Номер должен состоять только из цифр")
    if len(cart_numb_str) != 16:
        raise ValueError("Неверный номер карты")
    new_list = list()
    new_list.append(cart_numb_str[0:4])
    new_list.append(cart_numb_str[4:6] + "**")
    new_list.append("****")
    new_list.append(cart_numb_str[12:])
    return " ".join(new_list)


def get_mask_account(account_number: str) -> str:
    """Возвращает номер счета с маской"""
    account_number_str = str(account_number)
    if account_number == "":
        raise ValueError("Нет данных")
    if not account_number_str.isdigit():
        raise ValueError("Номер должен состоять только из цифр")
    if len(account_number_str) != 20:
        raise ValueError("Неверный номер счета")
    new_list = list()
    new_list.append("**" + account_number_str[-4:])
    return " ".join(new_list)


# Входные данные и их вывод для теста функций
# client_cart_number = 7000791119606365
# client_account_number = "73654108430135874305"
# # print(get_mask_card_number(str(client_cart_number)))
# print(get_mask_account(str(client_account_number)))
