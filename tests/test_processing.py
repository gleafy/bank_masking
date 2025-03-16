import pytest
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict, Any

@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T12:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-12-31T12:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-02T12:00:00.000000'},
    ]

def test_filter_by_state(transactions: List[Dict[str, Any]]) -> None:
    assert filter_by_state(transactions) == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T12:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-02T12:00:00.000000'},
    ]

def test_sort_by_date(transactions: List[Dict[str, Any]]) -> None:
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]['id'] == 3  # Самая новая дата
    assert sorted_transactions[-1]['id'] == 2  # Самая старая дата
