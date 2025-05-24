import os
import pytest
from src.decorators import log
from typing import Any


# Тестовые функции
@log()
def successful_func(a: int, b: int) -> int:
    """Функция для тестирования успешного выполнения"""
    return a + b


@log(filename="test_log.txt")
def failing_func(a: int, b: int) -> Any:
    """Функция для тестирования ошибок"""
    raise ValueError("Test error")


def test_console_logging(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирование логирования в консоль"""
    result = successful_func(2, 3)

    captured = capsys.readouterr()
    assert "successful_func ok" in captured.out
    assert "Result: 5" in captured.out
    assert result == 5


def test_file_logging() -> None:
    """Тестирование логирования в файл"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(ValueError):
        failing_func(1, 2)

    with open("test_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "failing_func error" in content
        assert "ValueError" in content
        assert "Inputs: (1, 2)" in content


def test_log_parameters() -> None:
    """Тестирование параметров декоратора"""
    assert successful_func.__name__ == "successful_func"
    assert successful_func.__doc__ == "Функция для тестирования успешного выполнения"
