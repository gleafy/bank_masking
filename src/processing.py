"""
Модуль processing.
Содержит функции для обработки данных о банковских операциях.
"""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Оставляет операции с указанным state.

    :param transactions: Список операций.
    :param state: Значение для фильтрации (по умолчанию "EXECUTED").
    :return: Отфильтрованный список операций.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    :param transactions: Список операций с ключом "date".
    :param reverse: Если True, сортирует по убыванию.
    :return: Отсортированный список.
    """
    return sorted(transactions, key=lambda x: datetime.fromisoformat(x.get("date", "")), reverse=reverse)
