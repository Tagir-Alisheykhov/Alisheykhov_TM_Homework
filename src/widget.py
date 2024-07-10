from src.masks import get_mask_card_number, get_mask_account


# Примеры входных данных:
cart_and_account_numbers = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """

date = "2018-08-11TO2:26:18.671407"


def mask_account_cart(type_and_number_cart: str) -> str:
    """
    Функция принимает тип и номер карты
    или номер счета выводя их замаскированными. Если номер карты введен неверно,
    то программа выдает ошибку
    """
    split_numbers_cart = type_and_number_cart.split()
    new_list = []
    name_and_number = []
    for numb_or_name in split_numbers_cart:
        if numb_or_name.isalpha():
            name_and_number.append(numb_or_name)
        elif numb_or_name.isdigit():
            if len(numb_or_name) == 16:
                masks_numb_cart = get_mask_card_number(numb_or_name)
                name_and_number.append(masks_numb_cart)
                new_list.append(name_and_number)
                name_and_number = list()
            elif len(numb_or_name) == 20:
                masks_numb_account = get_mask_account(numb_or_name)
                name_and_number.append(masks_numb_account)
                new_list.append(name_and_number)
                name_and_number = list()
            else:
                raise ValueError("Неправильное количество цифр в номере")
    ready_data = ""
    for values_cart in new_list:
        translate_into_a_line = " ".join(values_cart)
        ready_data += translate_into_a_line + "\n"
    return ready_data[:-1]


def get_data(raw_date: str) -> str:
    """
    Функция, которая принимает данные о дате
    и прочее, выводя только дату
    """
    index_symbol = raw_date.index("T")
    cut_raw_date = raw_date[:index_symbol]
    date_clear = ""
    if len(cut_raw_date) != 10:
        raise ValueError("Неверные данные")
    else:
        for one_symbol in raw_date:
            if one_symbol == "T":
                break
            elif one_symbol.isdigit():
                date_clear += one_symbol
            elif not one_symbol.isdigit():
                date_clear += " "
    date_clear_split = date_clear.split()
    split_date = date_clear_split[::-1]
    final_result = ".".join(split_date)
    return final_result


if __name__ == "__main__":
    print(mask_account_cart(cart_and_account_numbers))
    print(get_data(date))
