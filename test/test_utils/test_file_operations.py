from pathlib import Path

from src.utils.file_operations import read_json_file


def test_read_valid_json(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text('[{"id": 1}, {"id": 2}]')
    assert read_json_file(str(file)) == [{"id": 1}, {"id": 2}]


def test_read_invalid_json(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text("invalid json")
    assert read_json_file(str(file)) == []


def test_read_non_list_json(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text('{"id": 1}')
    assert read_json_file(str(file)) == []


def test_read_nonexistent_file() -> None:
    assert read_json_file("nonexistent.json") == []
