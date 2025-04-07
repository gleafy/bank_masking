"""
Модуль masks.
Содержит функции для маскировки номеров банковских карт и счетов.
"""

import logging
import os
from typing import Union

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Принимает номер карты в виде целого числа и возвращает маску номера в формате:
    XXXX XX** **** XXXX.
    """
    s = str(card_number).zfill(16)
    if len(s) != 16:
        logger.error(f"Некорректная длина номера карты: {card_number}")
        return "Некорректный номер карты"

    group1 = s[0:4]
    group2 = s[4:6] + "**"
    group3 = "****"
    group4 = s[12:16]
    logger.info(f"Успешно замаскирован номер карты: {card_number}")
    return f"{group1} {group2} {group3} {group4}"


def get_mask_account(account_number: int) -> str:
    """
    Принимает номер счета в виде целого числа и возвращает маску номера в формате:
    **XXXX.
    """
    s = str(account_number)
    if len(s) < 4:
        logger.error(f"Некорректный номер счета: {account_number}")
        return "Некорректный номер счета"

    logger.info(f"Успешно замаскирован номер счета: {account_number}")
    return "**" + s[-4:]
