import json
from src.utils import processing_json_file, sum_transactions
import pytest

mini_file_json = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
                  "Homework_Alisheykhov_TM/data_for_tests/mini_operations.json")
invalid_keys_file_json = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
                          "Homework_Alisheykhov_TM/data_for_tests/invalid_keys_in_operation.json")
invalid_code_currency_json = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
                              "Homework_Alisheykhov_TM/data_for_tests/invalid_code_currency_in_operation.json")
invalid_empty_file = ("C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/"
                      "Homework_Alisheykhov_TM/data_for_tests/invalid_code_currency_in_operation.json")


def open_file_with_tests_transactions():
    """Данные для теста корректности работы функции processing_json_file"""
    with open(mini_file_json, encoding='UTF-8') as f:
        json_file = json.load(f)
    return json_file


def test_processing_json_file():
    """Проверка на корректность работы функции processing_json_file"""
    assert processing_json_file(mini_file_json) == filtered_data


def test_invalid_value_in_processing_json_file():
    """Проверка вызова исключения при отсутствии обязательного ключа"""
    with pytest.raises(KeyError):
        assert processing_json_file(invalid_keys_file_json)


def test_invalid_code_currency_in_processing_json_file():
    """Проверка вызова исключения при неправильном коде валюты"""
    with pytest.raises(ValueError):
        assert processing_json_file(invalid_code_currency_json)


def test_invalid_empty_in_processing_json_file():
    """Проверка вызова исключения при неправильном коде валюты"""
    with pytest.raises(ValueError):
        assert processing_json_file(invalid_empty_file)


def test_sum_transactions():
    """Проверка корректности работы функции sum_transactions"""
    assert sum_transactions(filtered_data) == result_sum_all_operations


filtered_data = open_file_with_tests_transactions()
result_sum_all_operations = sum_transactions(filtered_data)
