import os
from os import path
from functools import wraps
from typing import Any

base_path = path.join(path.dirname(path.dirname(__file__)), "logs/")


def log(filename: str) -> Any:
    """Логирование данных"""
    def real_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            try:
                print("Декоратор успешно запущен.")
                if filename == "":
                    raise SyntaxError("Строка аргумента не должна быть пустой")
                elif filename:
                    with open(os.path.join(base_path + filename), "a", encoding="UTF-8") as file:
                        file.write(f"/{func.__name__} - Запись файла прошла успешно\n")
            except SyntaxError as err_1:
                print(f"{func.__name__} error: {err_1}. inputs: {args}, {kwargs}")
            print("Конец работы декоратора.")
            return result
        return wrapper
    return real_decorator


@log(filename="my_log.txt")
def my_function(digit1: int, digit2: int) -> int:
    """Сложение чисел"""
    return digit1 + digit2


if __name__ == "__main__":
    my_function(1, 2)
