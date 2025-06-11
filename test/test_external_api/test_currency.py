import sys
from pathlib import Path
from typing import Any
from typing import Dict
from unittest.mock import patch

import pytest
from src.external_api.currency import convert_to_rub

# Добавляем src в путь Python для корректного импорта
sys.path.append(str(Path(__file__).parent.parent.parent))


@pytest.fixture
def rub_transaction() -> Dict[str, Any]:
    return {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}


@pytest.fixture
def usd_transaction() -> Dict[str, Any]:
    return {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}


def test_convert_rub(rub_transaction: Dict[str, Any]) -> None:
    with patch("src.external_api.currency.get_exchange_rates") as mock_get:
        result = convert_to_rub(rub_transaction)
        assert result == 100.0
        mock_get.assert_not_called()


def test_convert_usd(usd_transaction: Dict[str, Any]) -> None:
    with patch("src.external_api.currency.get_exchange_rates") as mock_get:
        mock_get.return_value = {"USD": 0.01333}
        result = convert_to_rub(usd_transaction)
        assert pytest.approx(result, 0.1) == 750.0
        mock_get.assert_called_once()


def test_api_error(usd_transaction: Dict[str, Any]) -> None:
    with patch("src.external_api.currency.get_exchange_rates") as mock_get:
        mock_get.side_effect = ValueError("Ошибка API: Connection error")
        with pytest.raises(ValueError, match="Ошибка API: Connection error"):
            convert_to_rub(usd_transaction)


def test_missing_api_key(usd_transaction: Dict[str, Any]) -> None:
    with patch("os.getenv", return_value=None):
        with pytest.raises(ValueError, match="API ключ не настроен"):
            convert_to_rub(usd_transaction)


def test_unknown_currency(usd_transaction: Dict[str, Any]) -> None:
    with patch("src.external_api.currency.get_exchange_rates") as mock_get:
        mock_get.return_value = {"EUR": 0.011}
        with pytest.raises(ValueError, match="Неизвестная валюта: USD"):
            convert_to_rub(usd_transaction)
