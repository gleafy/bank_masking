import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    (1111222233334444, "1111 22** **** 4444"),
])
def test_get_mask_card_number(card_number: int | str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    (73654108430135874305, "**4305"),
    (123456, "**3456"),
    (987654321, "**4321"),
])
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected
