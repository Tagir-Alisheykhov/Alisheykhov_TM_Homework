import pytest
from src.widget import mask_account_cart, get_data
 # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
  # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
   # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
    # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
     # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
      # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
       # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ

@pytest.mark.parametrize("type_and_number_cart, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589")])
def test_mask_account_cart(type_and_number_cart, expected):
    """
    Тесты для проверки, что функция корректно распознает и
    применяет нужный тип маскировки в зависимости от типа входных данных
    (карта или счет)
    """
    assert mask_account_cart(type_and_number_cart) == expected
    with pytest.raises(ValueError):
        assert mask_account_cart("Maestro 159683786870519932")


@pytest.mark.parametrize("data, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(data, expected):
    """
    Тестирование правильности преобразования даты и на вызов исключения
    """
    assert get_data(data) == expected
    with pytest.raises(ValueError):
        assert get_data("20180811dbvDSK>f.2:26:18LA.671407")
 # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
  # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
   # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
    # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
     # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
      # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
       # ПРОВЕРКА ОТСУТСТВИЯ ДАННЫХ
