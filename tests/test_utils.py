from pathlib import Path
from src.utils import read_json
from typing import List, Dict, Any


def test_read_json_valid_file(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text('[{"id": 1}]')
    result: List[Dict[str, Any]] = read_json(str(file))
    assert result == [{"id": 1}]


def test_read_json_invalid_file(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text("invalid json")
    result: List[Dict[str, Any]] = read_json(str(file))
    assert result == []
