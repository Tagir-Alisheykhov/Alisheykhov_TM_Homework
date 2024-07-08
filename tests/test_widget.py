import pytest
from src.widget import mask_account_cart, get_data


@pytest.mark.parametrize("type_and_number_cart, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
])
def test_mask_account_cart(type_and_number_cart, expected):
    assert mask_account_cart(type_and_number_cart) == expected


@pytest.mark.parametrize("data, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(data, expected):
    assert get_data(data) == expected
