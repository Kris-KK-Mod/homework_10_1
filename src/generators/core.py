from typing import Any
from typing import Dict
from typing import Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по коду валюты.
    :param transactions: Список транзакций.
    :param currency_code: Код валюты (например, "USD").
    :return: Итератор с подходящими транзакциями.
    :raises: ValueError: Если currency_code пуст.
    """
    if not currency_code:
        raise ValueError("Код валюты не может быть пустым.")

    for transaction in transactions:
        try:
            op_amount = transaction.get("operationAmount", {})
            curr = op_amount.get("currency", {}).get("code", "").upper()
            if curr == currency_code.upper():
                yield transaction
        except (AttributeError, KeyError):
            continue  # Пропускаем битые транзакции


def transaction_descriptions(transactions: list[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.
    :param transactions: Список транзакций.
    :return: Итератор с описаниями.
    :raises: KeyError: Если у транзакции нет поля 'description'.
    """
    for transaction in transactions:
        if "description" not in transaction:
            raise KeyError(f"Транзакция {transaction.get('id')} не содержит поля 'description'.")
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Generates card numbers in format "XXXX 0000 0000 0000".
    :param start: first 4 digits (1-9999)
    :param end: last 4 digits (1-9999)
    :return: card number iterator
    """
    if start < 1 or end > 9999:
        raise ValueError("Range must be between 1 and 9999")

    for num in range(start, end + 1):
        yield f"{num:04d} 0000 0000 0000"
