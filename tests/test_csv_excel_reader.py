from unittest.mock import mock_open, patch
from typing import Any
import pandas as pd

from src.csv_excel_reader import read_csv, read_excel

CSV_DATA = """id;amount;currency
1;100;USD
2;200;EUR
"""

EXCEL_DATA = [
    {"id": 1, "amount": 100, "currency": "USD"},
    {"id": 2, "amount": 200, "currency": "EUR"},
]

def test_read_csv() -> None:
    with patch("builtins.open", mock_open(read_data=CSV_DATA)):
        result = read_csv("dummy.csv")
        assert len(result) == 2
        assert result[0]["id"] == "1"

@patch("pandas.read_excel")
def test_read_excel(mock_read: Any) -> None:
    mock_read.return_value = pd.DataFrame(EXCEL_DATA)
    result = read_excel("dummy.xlsx")
    assert len(result) == 2
    assert result[0]["id"] == 1