import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]


def test_filter_by_currency(transactions: list[dict]) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert len(list(usd_transactions)) == 2


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list[str]) -> None:
    assert list(card_number_generator(start, end)) == expected


def test_transaction_descriptions() -> None:
    transactions = [{"description": "Payment"}, {"description": "Transfer"}]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Payment"
    assert next(descriptions) == "Transfer"
