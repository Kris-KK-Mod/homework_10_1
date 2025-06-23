import pandas as pd
from pathlib import Path
from typing import List, Dict, Union
from . import utils_logger


def _convert_to_json_format(data: List[Dict]) -> List[Dict]:
    """Конвертирует структуру CSV/Excel в формат JSON."""
    converted = []
    for row in data:
        # Проверяем, что есть необходимые поля
        if not all(key in row for key in ['id', 'amount', 'currency_code']):
            continue

        converted_row = {
            "id": row.get("id"),
            "state": row.get("state", ""),
            "date": row.get("date", ""),
            "operationAmount": {
                "amount": str(row.get("amount", "")),
                "currency": {
                    "name": row.get("currency_name", ""),
                    "code": row.get("currency_code", "")
                }
            },
            "description": row.get("description", ""),
            "from": row.get("from", ""),
            "to": row.get("to", "")
        }
        converted.append(converted_row)
    return converted


def read_csv_file(file_path: Union[str, Path]) -> List[Dict]:
    """Читает CSV-файл и возвращает список транзакций в формате JSON."""
    try:
        data = pd.read_csv(file_path, sep=';').to_dict('records')
        result = _convert_to_json_format(data)
        utils_logger.info(f"Успешно прочитан CSV файл {file_path}. Найдено {len(result)} записей")
        return result
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении CSV файла {file_path}: {str(e)}", exc_info=True)
        return []


def read_excel_file(file_path: Union[str, Path]) -> List[Dict]:
    """Читает Excel-файл и возвращает список транзакций в формате JSON."""
    try:
        data = pd.read_excel(file_path).to_dict('records')
        result = _convert_to_json_format(data)
        utils_logger.info(f"Успешно прочитан Excel файл {file_path}. Найдено {len(result)} записей")
        return result
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении Excel файла {file_path}: {str(e)}", exc_info=True)
        return []
