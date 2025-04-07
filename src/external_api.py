"""
Модуль external_api.
Содержит функции для конвертации валют через внешнее API.
"""

import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: Dict[str, Any]) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли по текущему курсу валют.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма в рублях (тип float), округленная до 2 знаков после запятой.
    :raises ValueError: Если API-ключ не найден в переменных окружения.
    :raises ConnectionError: Если произошла ошибка при запросе к API.
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        raise ValueError("API key not found in .env")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.get(url, headers={"apikey": api_key})

    if response.status_code != 200:
        raise ConnectionError(f"API error: {response.text}")

    result: float = response.json()["result"]  # Явная аннотация типа
    return round(result, 2)
