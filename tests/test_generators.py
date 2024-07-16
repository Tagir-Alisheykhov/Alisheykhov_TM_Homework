from src.generators import filter_by_currency, transactions, transaction_descriptions

import pytest


@pytest.fixture
def values_for_filter_by_currency():
    """
    Неправильные входные значения для 'test_filter_by_currency_different_keys',
    где ключи <name> и <code> отличаются друг от друга
    """
    values = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]
    return values


@pytest.fixture
def virus_1():
    """ Ошибочные входные данные для 'test_filter_by_currency_no_required_keys' """
    value = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "<<<VIRUS>>>_operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]
    return value


@pytest.fixture
def virus_2():
    """ Ошибочные входные данные для 'test_filter_by_currency_no_required_keys' """
    value = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "<<<VIRUS>>>currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]
    return value


@pytest.fixture
def virus_3():
    """ Ошибочные входные данные для 'test_filter_by_currency_no_required_keys' """
    value = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "currency": {"<<<VIRUS>>>name": "USD", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]
    return value


@pytest.fixture
def virus_4():
    """ Ошибочные входные данные для 'test_filter_by_currency_no_required_keys' """
    value = [{
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
          "description<<<<<<<<<<<--VIRUS-->>>>>>>>>>>": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]
    return value


def test_filter_by_currency():
    """ Тест на корректную работу функции генератора """
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
          "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}
    assert next(generator) == {
          "id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
          "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод со счета на счет",
          "from": "Счет 19708645243227258542",
          "to": "Счет 75651667383060284188"
                }


def test_filter_by_currency_no_required_keys(virus_1, virus_2, virus_3):
    """ Отсутствие обязательного ключа """
    generator_1 = filter_by_currency(virus_1, "USD")
    generator_2 = filter_by_currency(virus_2, "USD")
    generator_3 = filter_by_currency(virus_3, "USD")
    with pytest.raises(KeyError):
        next(generator_1)
    with pytest.raises(KeyError):
        next(generator_2)
    with pytest.raises(KeyError):
        next(generator_3)


def test_empty_filter_by_currency():
    """ Ошибка на пустой список """
    generator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(virus_4):
    """ Ошибка при отсутствии обязательного ключа <description> """
    generator = transaction_descriptions(virus_4)
    with pytest.raises(KeyError):
        next(generator)


def test_empty_transaction_descriptions():
    """ Ошибка на пустой список """
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


def test