from typing import List, Dict, Literal


def filter_by_state(
    data: List[Dict[str, str]],
    state: Literal["EXECUTED", "PENDING", "CANCELED"] = "EXECUTED",) -> List[Dict[str, str]]:
    """ Фильтрует список операций по их статусу. """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], ascending: bool = True) -> List[Dict[str, str]]:
    """ Сортирует список операций по дате. """
    return sorted(data, key=lambda x: x["date"], reverse=not ascending)
