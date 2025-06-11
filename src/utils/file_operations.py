import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

from . import utils_logger


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    """
    try:
        with Path(file_path).open(encoding="utf-8") as f:
            data = json.load(f)
            result = data if isinstance(data, list) else []

            utils_logger.info(f"Успешно прочитан файл {file_path}. " f"Найдено {len(result)} записей")
            return result

    except (FileNotFoundError, json.JSONDecodeError) as e:
        utils_logger.error(f"Ошибка при чтении файла {file_path}: {str(e)}", exc_info=True)
        return []
