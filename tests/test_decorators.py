from src.decorators import log


@log(filename="")
def func_for_test_1(digit1, digit2):
    """Функция для теста 1"""
    return digit1 + digit2


@log(filename="my_log.txt")
def func_for_test_2(digit1, digit2):
    """Функция для теста 2"""
    return digit1 + digit2


def test_my_func_output_1(capsys):
    """Захват вывода в консоль. Вариант 1"""
    func_for_test_1(1, 3)
    out, err = capsys.readouterr()
    assert out == ('Декоратор успешно запущен.\n'
                   'func_for_test_1 error: Строка аргумента не должна быть пустой. inputs: (1, 3), {}\n'
                   'Конец работы декоратора.\n')
    assert err == ""


def test_my_func_output_2(capsys):
    """Захват вывода в консоль. Вариант 2"""
    func_for_test_2(1, 3)
    out, err = capsys.readouterr()
    assert out == 'Декоратор успешно запущен.\nКонец работы декоратора.\n'
    assert err == ""
