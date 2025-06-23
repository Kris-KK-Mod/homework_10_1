from typing import List
from typing import Literal

import pytest
from src.processing import filter_by_state
from src.processing import process_bank_operations
from src.processing import process_bank_search
from src.processing import sort_by_date
from src.types import Operation


def create_operation(
    op_id: int,
    state: Literal["EXECUTED", "PENDING", "CANCELED"],
    date: str,
    amount: str,
    currency: str,
    description: str,
    from_: str,
    to: str,
) -> Operation:
    return {
        "id": op_id,
        "state": state,
        "date": date,
        "operationAmount": {"amount": amount, "currency": {"code": currency}},
        "description": description,
        "from_": from_,
        "to": to,
    }


@pytest.fixture
def sample_ops() -> List[Operation]:
    return [
        create_operation(1, "EXECUTED", "2024-01-01", "100", "RUB", "Перевод", "Счет 1", "Счет 2"),
        create_operation(2, "EXECUTED", "2024-01-02", "200", "USD", "Вклад", "Счет 3", "Счет 4"),
        create_operation(3, "CANCELED", "2024-01-03", "300", "EUR", "Перевод", "Карта 1", "Счет 5"),
        create_operation(4, "PENDING", "2024-01-04", "400", "RUB", "", "Карта 2", "Счет 6"),
    ]


@pytest.fixture
def minimal_ops() -> List[Operation]:
    return [
        create_operation(1, "EXECUTED", "2024-03-11", "0", "RUB", "", "", ""),
        create_operation(2, "PENDING", "2024-03-10", "0", "RUB", "", "", ""),
        create_operation(3, "EXECUTED", "2024-03-09", "0", "RUB", "", "", ""),
        create_operation(4, "CANCELED", "2024-03-08", "0", "RUB", "", "", ""),
    ]


def test_search_normal_case(sample_ops: List[Operation]) -> None:
    search_result = process_bank_search(sample_ops, "перевод")
    assert len(search_result) == 2
    assert all("перевод" in op["description"].lower() for op in search_result)


def test_search_with_invalid_data() -> None:
    empty_list: List[Operation] = []
    invalid_item = [create_operation(1, "EXECUTED", "2024-01-01", "100", "RUB", "Test", "From", "To")]
    assert process_bank_search(empty_list, "test") == []
    assert process_bank_search(invalid_item, "") == []


def test_count_categories(sample_ops: List[Operation]) -> None:
    stats = process_bank_operations(sample_ops, ["вклад", "перевод"])
    # Приводим ключи к нижнему регистру для сравнения
    lower_stats = {k.lower(): v for k, v in stats.items()}
    assert lower_stats["вклад"] == 1
    assert lower_stats["перевод"] == 2


@pytest.mark.parametrize(
    "state,expected_count",
    [
        ("EXECUTED", 2),
        ("PENDING", 1),
        ("CANCELED", 1),
    ],
)
def test_filter_by_state(
    minimal_ops: List[Operation], state: Literal["EXECUTED", "PENDING", "CANCELED"], expected_count: int
) -> None:
    filtered = filter_by_state(minimal_ops, state)
    assert len(filtered) == expected_count
    if expected_count > 0:
        assert all(op["state"] == state for op in filtered)


@pytest.mark.parametrize(
    "ascending,expected_first_date",
    [
        (True, "2024-03-08"),
        (False, "2024-03-11"),
    ],
)
def test_sort_by_date(minimal_ops: List[Operation], ascending: bool, expected_first_date: str) -> None:
    sorted_ops = sort_by_date(minimal_ops, ascending=ascending)
    assert sorted_ops[0]["date"].startswith(expected_first_date)


def test_edge_cases() -> None:
    empty_list: List[Operation] = []
    single_item = [create_operation(1, "EXECUTED", "2024-01-01", "100", "RUB", "Test", "From", "To")]
    assert len(filter_by_state(empty_list, "EXECUTED")) == 0
    assert len(filter_by_state(single_item, "EXECUTED")) == 1
    assert len(sort_by_date(empty_list)) == 0
    assert len(sort_by_date(single_item)) == 1
