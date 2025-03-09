"""
Модуль processing.
Содержит функции для обработки данных о банковских операциях.
"""

from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей с банковскими операциями по значению ключа 'state'.

    :param transactions: Список словарей с данными операций.
    :param state: Значение для ключа 'state', по которому производится фильтрация (по умолчанию "EXECUTED").
    :return: Новый список словарей, содержащий только те операции, у которых значение ключа 'state' равно переданному state.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей с банковскими операциями по дате.

    :param transactions: Список словарей, где каждый словарь содержит ключ 'date' в формате ISO.
    :param reverse: Логический флаг, задающий порядок сортировки. По умолчанию True (сортировка по убыванию, сначала самые новые операции).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x.get("date", "")),
        reverse=reverse
    )
