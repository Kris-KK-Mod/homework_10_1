from typing import Any
from typing import Dict
from typing import List

import pytest
from src.generators.core import card_number_generator
from src.generators.core import filter_by_currency
from src.generators.core import transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Fixture providing sample transaction data for tests."""
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.00", "currency": {"code": "USD", "name": "US Dollar"}},
            "description": "Payment 1",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200.00", "currency": {"code": "EUR", "name": "Euro"}},
            "description": "Payment 2",
        },
        {"id": 3, "description": "Payment 3"},  # Transaction without currency
    ]


def test_filter_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Test filtering transactions by currency code."""
    # USD filtering
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["id"] == 1

    # EUR filtering
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]["id"] == 2

    # Non-existent currency
    assert len(list(filter_by_currency(sample_transactions, "GBP"))) == 0

    # Empty list
    assert len(list(filter_by_currency([], "USD"))) == 0

    # Empty currency code error
    with pytest.raises(ValueError):
        list(filter_by_currency(sample_transactions, ""))


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Test extracting transaction descriptions."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2", "Payment 3"]

    # Test missing description
    with pytest.raises(KeyError):
        list(transaction_descriptions([{"id": 1}]))


def test_card_number_generator() -> None:
    """Test card number generator functionality."""
    # Generate 3 numbers
    cards = list(card_number_generator(1, 3))
    assert cards == ["0001 0000 0000 0000", "0002 0000 0000 0000", "0003 0000 0000 0000"]

    # Format check
    card = next(card_number_generator(9999, 9999))
    assert card == "9999 0000 0000 0000"

    # Invalid range
    with pytest.raises(ValueError):
        list(card_number_generator(0, 1))

    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000))


def test_filter_by_currency_edge_cases() -> None:
    """Test edge cases for currency filtering."""
    # Transaction with incomplete data
    assert len(list(filter_by_currency([{"operationAmount": {}}], "USD"))) == 0
    assert len(list(filter_by_currency([{"operationAmount": {"currency": {}}}], "USD"))) == 0
