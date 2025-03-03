"""
Модуль masks.
Содержит функции для маскировки номеров банковских карт и счетов.
"""


def get_mask_card_number(card_number: int) -> str:
    """
    Принимает номер карты в виде целого числа и возвращает маску номера в формате:
    XXXX XX** **** XXXX.
    """
    s = str(card_number).zfill(16)  # гарантируем 16 символов
    group1 = s[0:4]
    group2 = s[4:6] + "**"
    group3 = "****"
    group4 = s[12:16]
    return f"{group1} {group2} {group3} {group4}"


def get_mask_account(account_number: int) -> str:
    """
    Принимает номер счета в виде целого числа и возвращает маску номера в формате:
    **XXXX.
    """
    s = str(account_number)
    return "**" + s[-4:]
