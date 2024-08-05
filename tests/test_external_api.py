from src.external_api import currency_conversion
from unittest.mock import patch
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KEY_API')

headers = {
    "apikey": API_KEY
}


@patch('requests.get')
def test_currency_conversion(mock_get):
    """Тест функции конвертации валюты"""
    mock_get.return_value.json.return_value = {'result': 85.547234}
    assert currency_conversion('USD', 1) == 85.547234
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?"
                                     "to=RUB&from=USD&amount=1", headers=headers)


def test_invalid_status_code_in_conversion():
    """Неуспешный статус-код"""
    with pytest.raises(ValueError):
        currency_conversion('123', 1)








