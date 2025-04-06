"""
Модуль decorators.
Содержит декораторы для логирования функций.
"""

from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{start_time} - Вызов функции {func.__name__} с аргументами: {args}, {kwargs}\n"
            result = None
            error = None

            try:
                result = func(*args, **kwargs)
                status = "Успешно"
            except Exception as e:
                status = "Ошибка"
                error = str(e)
                raise
            finally:
                full_log = (
                    f"{log_message}" f"{start_time} - Результат: {status}" f"{f'. Ошибка: {error}' if error else ''}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(full_log)
                else:
                    print(full_log.strip())

            return result

        return wrapper

    return decorator
