import re
from typing import Dict
from typing import List
from typing import Literal

from src.types import Operation
from src.utils.logger import get_logger

logger = get_logger(__name__, "logs/processing.log")


def process_bank_search(data: List[Operation], search: str) -> List[Operation]:
    """Фильтрация операций по описанию с использованием regex"""
    if not isinstance(data, list):
        logger.error("Передан неверный тип данных (ожидается список)")
        return []

    if not search or not isinstance(search, str):
        logger.warning("Пустой или неверный поисковый запрос")
        return []

    try:
        pattern = re.compile(re.escape(search), re.IGNORECASE)
        result = [
            op for op in data if isinstance(op, dict) and op.get("description") and pattern.search(op["description"])
        ]
        logger.info(f"Поиск '{search}': найдено {len(result)} операций")
        return result
    except re.error as e:
        logger.error(f"Ошибка в regex-паттерне: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}", exc_info=True)

    return []


def process_bank_operations(data: List[Operation], categories: List[str]) -> Dict[str, int]:
    """Подсчет операций по категориям с обработкой ошибок"""
    if not isinstance(data, list):
        logger.error("Передан неверный тип данных (ожидается список)")
        return {}

    if not categories or not all(isinstance(c, str) for c in categories):
        logger.warning("Неверные категории для подсчета")
        return {}

    try:
        valid_ops = [op for op in data if isinstance(op, dict) and isinstance(op.get("description"), str)]

        if not valid_ops:
            logger.info("Нет операций с описанием для подсчета")
            return {}

        descriptions = [op["description"].lower() for op in valid_ops]
        result = {}

        for category in set(c.strip().lower() for c in categories if c.strip()):
            count = sum(1 for desc in descriptions if category in desc.lower())
            if count > 0:
                # Сохраняем категории в нижнем регистре для единообразия
                result[category.lower()] = count

        logger.info(f"Подсчет завершен: {result}")
        return result

    except Exception as e:
        logger.error(f"Ошибка подсчета: {e}", exc_info=True)
        return {}


def filter_by_state(
    data: List[Operation],
    state: Literal["EXECUTED", "PENDING", "CANCELED"] = "EXECUTED",
) -> List[Operation]:
    """Фильтрует список операций по их статусу."""
    return [item for item in data if item["state"] == state]


def sort_by_date(data: List[Operation], ascending: bool = True) -> List[Operation]:
    """Сортирует список операций по дате."""
    return sorted(data, key=lambda x: x["date"], reverse=not ascending)
