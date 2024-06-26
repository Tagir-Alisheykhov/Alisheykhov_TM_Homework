import masks


# Примеры входных данных:
cart_and_account_numbers = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """


def mask_account_cart(type_and_number_cart: str) -> str:
    """
    Функция принимает тип и номер карты
    или номер счета выводя их замаскированными
    """
    split_numbers_cart = type_and_number_cart.split()
    new_list = []
    name_and_number = []
    for numb_or_name in split_numbers_cart:
        if numb_or_name.isalpha():
            name_and_number.append(numb_or_name)
        elif numb_or_name.isdigit():
            if len(numb_or_name) == 16:
                masks_numb_cart = masks.get_mask_card_number(numb_or_name)
                name_and_number.append(masks_numb_cart)
                new_list.append(name_and_number)
                name_and_number = list()
            elif len(numb_or_name) == 20:
                masks_numb_account = masks.get_mask_account(numb_or_name)
                name_and_number.append(masks_numb_account)
                new_list.append(name_and_number)
                name_and_number = list()
        else:
            continue
    ready_data = ""
    for values_cart in new_list:
        translate_into_a_line = " ".join(values_cart)
        ready_data += (translate_into_a_line + "\n")
    return ready_data


print(mask_account_cart(cart_and_account_numbers))
