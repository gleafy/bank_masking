"""
Модуль utils.
Содержит вспомогательные функции для работы с файлами.
"""

import json
from typing import List, Dict, Any


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями. Если файл не найден,
    содержит не список или поврежден, возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
