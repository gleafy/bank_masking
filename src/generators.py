"""
Модуль generators.
Содержит генераторы для обработки данных транзакций.
"""

from typing import Any, Dict, Iterable, Iterator


def filter_by_currency(transactions: Iterable[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Возвращает итератор транзакций с заданной валютой.

    :param transactions: Список транзакций.
    :param currency: Код валюты (например, "USD").
    :return: Итератор транзакций.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    :param transactions: Список транзакций.
    :return: Итератор описаний.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    :param start: Начальное значение (включительно).
    :param end: Конечное значение (включительно).
    :return: Итератор номеров карт в формате "XXXX XXXX XXXX XXXX".
    """
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        formatted = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted
