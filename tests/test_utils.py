from src.utils import sum_transactions
from unittest.mock import patch
import pytest


# @patch()



















@pytest.fixture
def transact_rub():
    transact = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }]
    return transact


# def test_sum_transaction_true(transact_rub):
#     assert sum_transactions(transact_rub) == 31957.58
