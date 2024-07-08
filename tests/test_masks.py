import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("cart_numb, expected", [("7000792289606361", "7000 79** **** 6361")])
def test_cart_number_with_mask(cart_numb, expected):
    assert get_mask_card_number(cart_numb) == expected


@pytest.mark.parametrize("account_numb, expected", [("73654108430135874305", "**4305")])
def test_account_with_mask(account_numb, expected):
    assert get_mask_account(account_numb) == expected
