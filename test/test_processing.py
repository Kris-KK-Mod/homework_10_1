from typing import List
from typing import Literal
from typing import TypedDict

import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


class Operation(TypedDict):
    """Тип для представления банковской операции"""

    state: Literal["EXECUTED", "PENDING", "CANCELED"]
    date: str


@pytest.fixture
def operations_data() -> List[Operation]:
    """Фикстура с тестовыми операциями"""
    return [
        {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"state": "PENDING", "date": "2024-03-10T12:00:00.000000"},
        {"state": "EXECUTED", "date": "2024-03-09T08:15:27.123456"},
        {"state": "CANCELED", "date": "2024-03-08T18:30:45.654321"},
    ]


@pytest.mark.parametrize(
    "state,expected_count",
    [
        ("EXECUTED", 2),
        ("PENDING", 1),
        ("CANCELED", 1),
        ("UNKNOWN", 0),
    ],
    ids=["executed", "pending", "canceled", "unknown"],
)
def test_filter_by_state(
    operations_data: List[Operation],
    state: Literal["EXECUTED", "PENDING", "CANCELED"],  # Исправленный тип
    expected_count: int,
) -> None:  # Добавлен возвращаемый тип
    """Тестирование фильтрации по статусу операции"""
    result = filter_by_state(operations_data, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(op["state"] == state for op in result)


@pytest.mark.parametrize(
    "ascending,expected_first_date",
    [
        (True, "2024-03-08"),
        (False, "2024-03-11"),
    ],
    ids=["ascending", "descending"],
)
def test_sort_by_date(
    operations_data: List[Operation], ascending: bool, expected_first_date: str
) -> None:  # Добавлен возвращаемый тип
    """Тестирование сортировки по дате"""
    sorted_ops = sort_by_date(operations_data, ascending=ascending)
    assert sorted_ops[0]["date"].startswith(expected_first_date)


@pytest.mark.parametrize(
    "input_data,expected_length",
    [
        ([], 0),
        ([{"state": "EXECUTED", "date": "2024-01-01T00:00:00.000000"}], 1),
    ],
    ids=["empty_list", "single_item"],
)
def test_edge_cases(input_data: List[Operation], expected_length: int) -> None:  # Добавлен возвращаемый тип
    """Тестирование граничных случаев"""
    assert len(filter_by_state(input_data, "EXECUTED")) == (
        expected_length if "EXECUTED" in [op.get("state") for op in input_data] else 0
    )
    assert len(sort_by_date(input_data)) == expected_length
