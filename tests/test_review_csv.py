from pathlib import Path

from scripts.review_csv import review_csv


def test_valid_csv(tmp_path):
    csv_path = tmp_path / "valid.csv"
    csv_path.write_text("record_id,status\nA-001,complete\nA-002,complete\n", encoding="utf-8")

    result = review_csv(csv_path, ("record_id", "status"))

    assert result.rows == 2
    assert result.blank_required_values == 0
    assert result.missing_columns == ()


def test_missing_required_column(tmp_path):
    csv_path = tmp_path / "missing.csv"
    csv_path.write_text("record_id\nA-001\n", encoding="utf-8")

    result = review_csv(csv_path, ("record_id", "status"))

    assert result.rows == 1
    assert result.blank_required_values == 0
    assert result.missing_columns == ("status",)


def test_blank_required_value(tmp_path):
    csv_path = tmp_path / "blank.csv"
    csv_path.write_text("record_id,status\nA-001,\nA-002,complete\n", encoding="utf-8")

    result = review_csv(csv_path, ("record_id", "status"))

    assert result.rows == 2
    assert result.blank_required_values == 1
    assert result.missing_columns == ()
