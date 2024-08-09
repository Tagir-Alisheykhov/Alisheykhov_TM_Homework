import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_cart_number_with_mask():
    """ Проверяет корректность маскировки номера банковской карты """
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_invalid_very_big_value_in_cart_number_with_mask():
    """ Проверка ошибки на слишком длинные входные данные номера карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("111111111111111111111111111")


def test_invalid_value_not_isdigit_in_cart_number_with_mask():
    """ Проверка ошибки, если номер карты состоит не только из цифр """
    with pytest.raises(ValueError):
        get_mask_card_number("70007922fg606361")


def test_invalid_number_with_mask_if_no_value():
    """ Проверка ошибки на пустую строку """
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_account_with_mask():
    """ Проверяет корректность маскировки номера счета """
    assert get_mask_account("73654108430135874305") == "**4305"


def test_invalid_get_account_cart_if_not_value():
    """ Ошибка, если строка пустая """
    with pytest.raises(ValueError):
        get_mask_account("")


def test_invalid_value_not_isdigit_in_account_with_mask():
    """ Проверка ошибки, если номер счета состоит не только из цифр """
    with pytest.raises(ValueError):
        get_mask_account("t11ig11t11x1oo1e1y1u")


def test_account_with_mask_invalid_size():
    """ Проверка ошибки на слишком длинные входные данные номера счета """
    with pytest.raises(ValueError):
        get_mask_account("222")
    with pytest.raises(ValueError):
        get_mask_account("2222222222222222222222")
