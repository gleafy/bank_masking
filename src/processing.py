from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:

    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:

    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x.get("date", "")),
        reverse=reverse
    )
