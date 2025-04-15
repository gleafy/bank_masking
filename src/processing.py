"""
Модуль processing.
Содержит функции для обработки данных о банковских операциях.
"""

import re
from collections import Counter
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


def search_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в описании которых встречается заданная строка (без учёта регистра).

    :param transactions: Список транзакций.
    :param search_string: Строка для поиска.
    :return: Отфильтрованный список транзакций.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_categories(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций для каждой категории.

    :param transactions: Список транзакций.
    :param categories: Список категорий для подсчёта.
    :return: Словарь {категория: количество}.
    """
    descriptions = [t.get("description", "") for t in transactions]
    return {category: count for category, count in Counter(descriptions).items() if category in categories}
