from typing import Any, Dict, List

import pytest

from src.processing import count_categories, filter_by_state, search_by_description, sort_by_date


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T12:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-31T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-02T12:00:00.000000"},
    ]


def test_filter_by_state(transactions: List[Dict[str, Any]]) -> None:
    assert filter_by_state(transactions) == [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-02T12:00:00.000000"},
    ]


def test_sort_by_date(transactions: List[Dict[str, Any]]) -> None:
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]["id"] == 3  # Самая новая дата
    assert sorted_transactions[-1]["id"] == 2  # Самая старая дата


def test_search_by_description() -> None:
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
    ]
    result = search_by_description(transactions, "организации")
    assert len(result) == 1


def test_count_categories() -> None:
    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]
    result = count_categories(transactions, ["Перевод с карты на карту"])
    assert result == {"Перевод с карты на карту": 2}
