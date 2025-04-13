"""
Модуль csv_excel_reader.
Содержит функции для чтения CSV и Excel файлов с транзакциями.
"""

import csv
import logging
import os
from typing import Any, Dict, List
import pandas as pd

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger("csv_excel_reader")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/csv_excel_reader.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список транзакций.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями. Если файл не найден или поврежден, возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            transactions = list(reader)
            logger.info(f"Успешно прочитан CSV-файл: {file_path}")
            return transactions
    except FileNotFoundError:
        logger.error(f"CSV-файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {str(e)}")
        return []


def read_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список транзакций.
    """
    try:
        df = pd.read_excel(file_path)
        transactions = []
        for item in df.to_dict("records"):
            new_dict = {}
            for k, v in item.items():
                new_dict[str(k)] = v  # Чтобы mypy не ругался
            transactions.append(new_dict)
        logger.info(f"Успешно прочитан Excel-файл: {file_path}")
        return transactions
    except FileNotFoundError:
        logger.error(f"Excel-файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {str(e)}")
        return []