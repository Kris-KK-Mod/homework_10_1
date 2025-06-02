import os
import requests
from typing import Dict, Any, cast
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        if currency == 'RUB':
            return amount

        rates = get_exchange_rates()
        rate = rates.get(currency)

        if not rate:
            raise ValueError(f"Неизвестная валюта: {currency}")

        return round(amount / rate, 2)
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Не удалось конвертировать валюту: {str(e)}")


def get_exchange_rates() -> Dict[str, float]:
    """Получает текущие курсы валют от API"""
    api_key = os.getenv('EXCHANGE_RATE_API_KEY')
    if not api_key:
        raise ValueError("API ключ не настроен")

    try:
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            headers={'apikey': api_key},
            params={'base': 'RUB'},
            timeout=10
        )
        response.raise_for_status()
        return cast(Dict[str, float], response.json()['rates'])
    except Exception as e:
        raise ValueError(f"Ошибка API: {str(e)}")
