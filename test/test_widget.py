import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def card_samples():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456")
    ]

@pytest.fixture
def account_samples():
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 12345678901234567890", "Account **7890")
    ]

@pytest.fixture
def invalid_samples():
    return [
        ("", "Ошибка: строка должна содержать тип и номер"),
        ("Card", "Ошибка: строка должна содержать тип и номер")
    ]

@pytest.fixture
def date_samples():
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-31T23:59:59.999999", "31.12.2025")
    ]

@pytest.fixture
def invalid_dates():
    return ["", "invalid-date", "2024/03/11"]

@pytest.mark.parametrize(
    "input_str,expected",
    [
        # Карты
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        # Счета
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 12345678901234567890", "Account **7890"),
        # Невалидные данные
        ("", "Ошибка: строка должна содержать тип и номер"),
        ("Счет", "Ошибка: строка должна содержать тип и номер"),
        ("Maestro1234567890123456", "Ошибка: строка должна содержать тип и номер"),
    ],
    ids=[
        "valid_visa_card",
        "valid_maestro_card",
        "valid_russian_account",
        "valid_english_account",
        "empty_input",
        "account_type_only",
        "card_without_space"
    ]
)
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize(
    "date_str,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
        ("неправильная дата", "Ошибка: неверный формат даты"),
        ("", "Ошибка: неверный формат даты"),
        ("2024/03/11", "Ошибка: неверный формат даты"),
    ],
    ids=[
        "valid_datetime_1",
        "valid_datetime_2",
        "invalid_text_date",
        "empty_date",
        "invalid_date_format"
    ]
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
