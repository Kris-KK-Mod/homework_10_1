from src.masks.masking import get_mask_account
from src.masks.masking import get_mask_card_number


def test_card_masking():
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234") == "Ошибка: номер карты должен содержать минимум 10 цифр"


def test_account_masking():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("123") == "Ошибка: номер счёта должен содержать минимум 4 цифры"
