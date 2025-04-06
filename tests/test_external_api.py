from unittest.mock import patch, Mock
import pytest
from src.external_api import convert_currency
from typing import Dict, Any


@patch.dict("os.environ", {"EXCHANGE_API_KEY": "test_key"})
@patch("requests.get")
def test_convert_currency_usd(mock_get: Mock) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 75.5}
    mock_get.return_value = mock_response

    transaction: Dict[str, Any] = {"operationAmount": {"amount": "1.0", "currency": {"code": "USD"}}}
    assert convert_currency(transaction) == 75.5


@patch.dict("os.environ", {"EXCHANGE_API_KEY": "test_key"})
@patch("requests.get")
def test_convert_currency_error(mock_get: Mock) -> None:
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    transaction: Dict[str, Any] = {"operationAmount": {"amount": "1.0", "currency": {"code": "USD"}}}
    with pytest.raises(ConnectionError):
        convert_currency(transaction)
