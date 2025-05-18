from src import get_mask_account
import pytest

from src import get_mask_card_number


def test_card_masking():
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234") == "Ошибка: номер карты должен содержать минимум 10 цифр"


def test_account_masking():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("123") == "Ошибка: номер счёта должен содержать минимум 4 цифры"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # стандартный номер
        ("1234567890123456", "1234 56** **** 3456"),  # другой номер
        ("1234", "Ошибка: номер карты должен содержать минимум 10 цифр"),  # короткий номер
        ("7000 7922 8960 6361", "7000 79** **** 6361"),  # с пробелами
        ("", "Ошибка: номер карты должен содержать минимум 10 цифр"),  # пустая строка
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # стандартный номер
        ("1234567890123456", "1234 56** **** 3456"),  # другой номер
        ("1234", "Ошибка: номер карты должен содержать минимум 10 цифр"),  # короткий номер
        ("7000 7922 8960 6361", "7000 79** **** 6361"),  # с пробелами
        ("", "Ошибка: номер карты должен содержать минимум 10 цифр"),  # пустая строка
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),  # нормальный счёт
        ("1234", "**1234"),  # минимальная длина
        ("123", "Ошибка: номер счёта должен содержать минимум 4 цифры"),  # слишком короткий
        ("", "Ошибка: номер счёта должен содержать минимум 4 цифры"),  # пустая строка
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


@pytest.fixture
def valid_card_numbers():
    """Фикстура с валидными номерами карт"""
    return [
        "7000792289606361",
        "1234567890123456",
        "5999123456789012"
    ]

@pytest.fixture
def invalid_card_numbers():
    """Фикстура с невалидными номерами карт"""
    return ["", "1234", "abcdefghijk"]

@pytest.fixture
def valid_account_numbers():
    """Фикстура с валидными номерами счетов"""
    return [
        "73654108430135874305",
        "12345678901234567890",
        "98765432109876543210"
    ]

@pytest.fixture
def invalid_account_numbers():
    """Фикстура с невалидными номерами счетов"""
    return ["", "123", "abcde"]

def test_get_mask_card_number_valid(valid_card_numbers):
    for number in valid_card_numbers:
        masked = get_mask_card_number(number)
        assert len(masked) == 19  # Проверяем формат маскировки
        assert "****" in masked

def test_get_mask_card_number_invalid(invalid_card_numbers):
    for number in invalid_card_numbers:
        assert "Ошибка" in get_mask_card_number(number)

def test_get_mask_account_valid(valid_account_numbers):
    for number in valid_account_numbers:
        masked = get_mask_account(number)
        assert masked.startswith("**")
        assert len(masked) == 6  # Формат **XXXX

def test_get_mask_account_invalid(invalid_account_numbers):
    for number in invalid_account_numbers:
        assert "Ошибка" in get_mask_account(number)


@pytest.mark.parametrize(
    "number,expected",
    [
        pytest.param("7000792289606361", "7000 79** **** 6361", id="valid_16_digit"),
        pytest.param("1234567890123456", "1234 56** **** 3456", id="another_16_digit"),
        pytest.param("1234", "Ошибка: номер карты должен содержать минимум 10 цифр", id="too_short"),
        pytest.param("", "Ошибка: номер карты должен содержать минимум 10 цифр", id="empty_string"),
        pytest.param("7000 7922 8960 6361", "7000 79** **** 6361", id="with_spaces"),
    ],
)
def test_get_mask_card_number(number: str, expected: str):
    assert get_mask_card_number(number) == expected

@pytest.mark.parametrize(
    "account,expected",
    [
        pytest.param("73654108430135874305", "**4305", id="valid_account"),
        pytest.param("12345678901234567890", "**7890", id="another_account"),
        pytest.param("1234", "**1234", id="min_length"),
        pytest.param("123", "Ошибка: номер счёта должен содержать минимум 4 цифры", id="too_short"),
        pytest.param("", "Ошибка: номер счёта должен содержать минимум 4 цифры", id="empty_string"),
    ],
)
def test_get_mask_account(account: str, expected: str):
    assert get_mask_account(account) == expected


# Дополнительные тесты для edge cases
def test_get_mask_card_number_with_non_digits():
    assert get_mask_card_number("7000 792a 8960 6361") == "7000 79** **** 6361"

def test_get_mask_account_whitespace():
    assert get_mask_account(" 73654108430135874305 ") == "**4305"
