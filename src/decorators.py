# Ожидаемый вывод в лог-файл mylog.txt
# при успешном выполнении:
# >>> my_function ok
#
# Ожидаемый вывод при ошибке:
# >>> my_function error: тип ошибки. Inputs: (1, 2), {}
#
# ---> Где "тип ошибки" заменяется на текст ошибки.
from functools import wraps
import os

base_path = "C:/Users/Lenovo/SkyProLearn2/SkyProject_2/Homework_AlisheykhovTM/Homework_Alisheykhov_TM/"
full_path_my_log = os.path.join(base_path + "logs", "my_log.txt")


def log(filename=None):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Декоратор успешно запущен.")
            result = func(*args, **kwargs)
            if filename:
                with open(full_path_my_log, "a", encoding="UTF-8") as file:
                    file.write(f"/{func.__name__} - Запись файла прошла успешно\n")
            else:
                print(f"{func.__name__} error: <Указать тип ошибки>. inputs: {args}, {kwargs}")
            print(f"Конец работы декоратора.")
            return result
        return wrapper
    return real_decorator


@log(filename="my_log.txt")
def my_function(x, y):
    """ Сложение чисел """
    return x + y


my_function(1, 2)

# ТЕСТИРОВАНИЕ

# 1 - РЕАЛИЗОВАТЬ ТЕСТИРОВАНИЕ НА "CAPSYS"
# 2 - РЕАЛИЗОВАТЬ ТЕСТИРОВАНИЕ НА РАЗНЫЕ СЦЕНАРИИ И НЕПРАВИЛЬНЫЕ ДАННЫЕ
# 3 - МОЖНО ДОБАВИТЬ ПРЕДИКАТ, ЕСЛИ НЕ НАПИСАН FILENAME
# 4 - НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ ВНУТРИ ФАЙЛ-НЕЙМ --> ТОЛЬКО СТРОКИ
# 5 - УКАЗАТЬ ТИП ОШИБКИ В ЛОГЕ, ЕСЛИ ВЫВОД В КОНСОЛЬ
# 6 - СДЕЛАТЬ "PULL-REQUEST"
