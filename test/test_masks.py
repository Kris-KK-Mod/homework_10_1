from typing import List

import pytest
from src import get_mask_account
from src import get_mask_card_number


def test_card_masking() -> None:
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234") == "Ошибка: номер карты должен содержать минимум 10 цифр"


def test_account_masking() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("123") == "Ошибка: номер счёта должен содержать минимум 4 цифры"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234", "Ошибка: номер карты должен содержать минимум 10 цифр"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("", "Ошибка: номер карты должен содержать минимум 10 цифр"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("1234", "**1234"),
        ("123", "Ошибка: номер счёта должен содержать минимум 4 цифры"),
        ("", "Ошибка: номер счёта должен содержать минимум 4 цифры"),
    ],
)
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected


@pytest.fixture
def valid_card_numbers() -> List[str]:
    return ["7000792289606361", "1234567890123456", "5999123456789012"]


@pytest.fixture
def invalid_card_numbers() -> List[str]:
    return ["", "1234", "abcdefghijk"]


@pytest.fixture
def valid_account_numbers() -> List[str]:
    return ["73654108430135874305", "12345678901234567890", "98765432109876543210"]


@pytest.fixture
def invalid_account_numbers() -> List[str]:
    return ["", "123", "abcde"]


def test_get_mask_card_number_valid(valid_card_numbers: List[str]) -> None:
    for number in valid_card_numbers:
        masked = get_mask_card_number(number)
        assert len(masked) == 19
        assert "****" in masked


def test_get_mask_card_number_invalid(invalid_card_numbers: List[str]) -> None:
    for number in invalid_card_numbers:
        assert "Ошибка" in get_mask_card_number(number)


def test_get_mask_account_valid(valid_account_numbers: List[str]) -> None:
    for number in valid_account_numbers:
        masked = get_mask_account(number)
        assert masked.startswith("**")
        assert len(masked) == 6


def test_get_mask_account_invalid(invalid_account_numbers: List[str]) -> None:
    for number in invalid_account_numbers:
        assert "Ошибка" in get_mask_account(number)


def test_get_mask_card_number_with_non_digits() -> None:
    assert get_mask_card_number("7000 792a 8960 6361") == "7000 79** **** 6361"


def test_get_mask_account_whitespace() -> None:
    assert get_mask_account(" 73654108430135874305 ") == "**4305"
