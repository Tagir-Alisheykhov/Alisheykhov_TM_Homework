import os
from typing import Any
from unittest.mock import patch

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("KEY_API")
headers = {"apikey": API_KEY}


def currency_conversion_for_test(currency: str = "USD", nominal: int = 1) -> Any:
    """Конвертация входной валюты в рубль"""
    response = requests.get(
        (f"https://api.apilayer.com/exchangerates_data/convert?" 
         f"to=RUB&from={currency}&amount={nominal}"),
        headers=headers,
    )
    result = response.json()["result"]
    return result


@patch("requests.get")
def test_currency_conversion(mock_get: Any) -> Any:
    """Тест функции конвертации валюты"""
    mock_get.return_value.json.return_value = {"result": 85.547234}
    assert currency_conversion_for_test("USD", 1) == 85.547234
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?" 
        "to=RUB&from=USD&amount=1", headers=headers
    )