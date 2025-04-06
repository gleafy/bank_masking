import os

import pytest

from src.decorators import log


@log()
def sample_function_console(a: int, b: int) -> int:
    return a + b


@log(filename="test_log.txt")
def sample_function_file(a: int, b: int) -> int:
    return a * b


@log()
def error_function() -> None:
    raise ValueError("Тестовая ошибка")


def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    sample_function_console(2, 3)
    captured = capsys.readouterr()
    assert "Вызов функции sample_function_console" in captured.out
    assert "Результат: Успешно" in captured.out


def test_log_to_file() -> None:
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    sample_function_file(2, 3)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Вызов функции sample_function_file" in content
    assert "Результат: Успешно" in content


def test_log_error(capsys: pytest.CaptureFixture) -> None:
    try:
        error_function()
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert "Результат: Ошибка" in captured.out
    assert "Ошибка: Тестовая ошибка" in captured.out
