import pytest
from src.widget import mask_account_cart, get_data


@pytest.mark.parametrize("type_and_number_cart, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589")])
def test_mask_account_cart(type_and_number_cart, expected):
    """
    Проверка универсальности функции - корректно распознает и
    применяет нужный тип маскировки в зависимости от типа входных данных
    (карта или счет)
    """
    assert mask_account_cart(type_and_number_cart) == expected


def test_maks_account_cart_invalid_empty_line():
    """ Ошибка на пустую строку """
    with pytest.raises(ValueError):
        mask_account_cart("")


def test_mask_account_cart_invalid_size_number():
    """
    Проверка того, что функция выдаст ошибку,
    если размер номера счета или карты слишком большой или маленький
    """
    with pytest.raises(ValueError):
        mask_account_cart("Maestro 15968378687051911111111")
    with pytest.raises(ValueError):
        mask_account_cart("Maestro 1")
    with pytest.raises(ValueError):
        mask_account_cart("Счет 6468647367889477958922222222")
    with pytest.raises(ValueError):
        mask_account_cart("Счет 2")


@pytest.mark.parametrize("data, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(data, expected):
    """ Проверка корректности преобразования даты """
    assert get_data(data) == expected


def test_get_data_quantity_values():
    """
    Проверка наличия всех трех значений, где Год, месяц и день
    - это три разных значения
    """
    with pytest.raises(ValueError):
        get_data("XXXX-07-11T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("-07-11T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("2018-XX-11T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("--T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("2018-08-XXT02:26:18.671407")


def test_get_data_invalid_size_year_month_day():
    """ Проверка на то, чтобы год, месяц и день были нужных размеров """
    with pytest.raises(ValueError):
        get_data("22-22-22T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("4444-1-22T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("4444-22-1T02:26:18.671407")


def test_get_data_invalid_size_year_month_day_isdigit():
    """ Проверка на то, чтобы год, месяц и день были цифрами """
    with pytest.raises(ValueError):
        get_data("XXXX-22-22T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("4444-XX-22T02:26:18.671407")
    with pytest.raises(ValueError):
        get_data("4444-22-XXT02:26:18.671407")


def test_get_data_invalid_presence_of_value_separators():
    """ Проверяет наличие разделителей между годом, месяцем и днем """
    with pytest.raises(ValueError):
        get_data("44442211T02:26:18.671407")


def test_get_data_invalid_empty_line():
    """ Ошибка на пустую строку """
    with pytest.raises(ValueError):
        get_data("")


def test_get_data_invalid_no_symbol_t():
    """
    Проверка отсутствия буквы 'Т' - означающую разделение
    между датой и временем во входных данных. Этот символ необходим, чтобы
    корректно изъять только дату, отбрасывая данные о времени
    """
    with pytest.raises(ValueError):
        get_data("2018-07-1102:26:18.671407")
