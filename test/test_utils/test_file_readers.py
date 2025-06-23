import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from src.utils.file_readers import read_csv_file, read_excel_file


@pytest.fixture
def mock_csv_data():
    return """id;state;date;amount;currency_name;currency_code;from;to;description
1;EXECUTED;2023-01-01;100;руб.;RUB;Карта 1234;Счет 5678;Перевод"""


@pytest.fixture
def mock_excel_data():
    return pd.DataFrame({
        "id": [1],
        "state": ["EXECUTED"],
        "date": ["2023-01-01"],
        "amount": [100],
        "currency_name": ["руб."],
        "currency_code": ["RUB"],
        "from": ["Карта 1234"],
        "to": ["Счет 5678"],
        "description": ["Перевод"]
    })


def test_read_csv_file(mock_csv_data):
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        with patch("pandas.read_csv") as mock_read_csv:
            # Создаем DataFrame с правильными данными
            mock_df = pd.DataFrame([{
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100,
                "currency_name": "руб.",
                "currency_code": "RUB",
                "from": "Карта 1234",
                "to": "Счет 5678",
                "description": "Перевод"
            }])
            mock_read_csv.return_value = mock_df

            result = read_csv_file("dummy.csv")
            assert isinstance(result, list)
            assert len(result) == 1
            assert result[0]["operationAmount"]["amount"] == "100"
            assert result[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_read_excel_file(mock_excel_data):
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = mock_excel_data
        result = read_excel_file("dummy.xlsx")
        assert isinstance(result, list)
        assert result[0]["operationAmount"]["amount"] == "100"
        assert result[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_read_csv_file_error():
    with patch("pandas.read_csv", side_effect=Exception("Error")):
        result = read_csv_file("invalid.csv")
        assert result == []


def test_read_excel_file_error():
    with patch("pandas.read_excel", side_effect=Exception("Error")):
        result = read_excel_file("invalid.xlsx")
        assert result == []
