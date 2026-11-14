# tests/test_loader.py
import pytest
from src.loader import load_bible


def test_normal_file_works(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("Genesis 1:1\tIn the beginning...\n", encoding="utf-8")

    assert load_bible(f) == "Genesis 1:1\tIn the beginning...\n"


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_bible(tmp_path / "nope.txt")


def test_empty_file_returns_empty_string(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("", encoding="utf-8")

    assert load_bible(f) == ""