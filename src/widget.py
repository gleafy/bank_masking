"""
Модуль widget.
Содержит функции для маскировки номера карты/счёта и форматирования даты.
"""

from datetime import datetime

from src import masks  # Импортируем функции маскировки из модуля masks


def mask_account_card(info: str) -> str:
    """
    Принимает одну строку, содержащую тип и номер карты/счёта.
    Пример входных данных:
        "Visa Platinum 7000792289606361"
        "Maestro 1596837868705199"
        "Счет 73654108430135874305"
    Функция определяет, является ли вход строкой для карты или счета,
    и возвращает строку с замаскированным номером, используя функции из модуля masks.

    Для карт формат: <тип карты> <маскированный номер карты>
    Пример: "Visa Platinum 7000 79** **** 6361"

    Для счета формат: "Счет <маскированный номер счета>"
    Пример: "Счет **4305"

    :param info: строка с типом и номером.
    :return: строка с замаскированным номером.
    """
    tokens = info.split()
    number_str = tokens[-1]
    prefix = " ".join(tokens[:-1])

    # Если префикс равен "Счет" (без учета регистра) — это счет
    if prefix.lower() == "счет":
        masked = masks.get_mask_account(int(number_str))
        return prefix + " " + masked
    else:
        masked = masks.get_mask_card_number(int(number_str))
        return prefix + " " + masked


def get_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате ISO (например, "2024-03-11T02:26:18.671407")
    и возвращает дату в формате "ДД.ММ.ГГГГ" (например, "11.03.2024").

    :param date_str: строка с датой в формате ISO.
    :return: строка с датой в формате "ДД.ММ.ГГГГ".
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
