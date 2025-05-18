from typing import List, Literal, TypedDict


class Operation(TypedDict):
    state: Literal["EXECUTED", "PENDING", "CANCELED"]
    date: str


def filter_by_state(
    data: List[Operation],
    state: Literal["EXECUTED", "PENDING", "CANCELED"] = "EXECUTED",
) -> List[Operation]:
    """
    Фильтрует список операций по их статусу.
    :rtype: object
    """
    return [item for item in data if item["state"] == state]


def sort_by_date(data: List[Operation], ascending: bool = True) -> List[Operation]:
    """
    Сортирует список операций по дате.
    """
    return sorted(data, key=lambda x: x["date"], reverse=not ascending)
