import json
import csv
import pytest
from src.lab05.json_csv import json_to_csv, csv_to_json


@pytest.mark.parametrize(
    "data",
    [
        [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25},
        ],
        [
            {"city": "Moscow", "year": 2024},
            {"city": "London", "year": 2025},
        ],
    ],
)
def test_json_to_csv_basic(tmp_path, data):
    src = tmp_path / "input.json"
    dst = tmp_path / "output.csv"

    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    json_to_csv(src, dst)

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == len(data)
    assert set(rows[0].keys()) == set(data[0].keys())


@pytest.mark.parametrize(
    "content",
    [
        "",
        "{}",
        "[]",
        "[1, 2, 3]",
    ],
)
def test_json_to_csv_invalid_json(tmp_path, content):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"

    src.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(src, dst)


@pytest.mark.parametrize(
    "src_name, dst_name, error",
    [
        ("data.txt", "out.csv", ValueError),
        ("data.json", "out.txt", ValueError),
        ("missing.json", "out.csv", FileNotFoundError),
    ],
)
def test_json_to_csv_path_errors(tmp_path, src_name, dst_name, error):
    src = tmp_path / src_name
    dst = tmp_path / dst_name

    if src_name != "missing.json":
        src.write_text("[]", encoding="utf-8")

    with pytest.raises(error):
        json_to_csv(src, dst)


@pytest.mark.parametrize(
    "rows",
    [
        [
            {"name": "Alice", "age": "22"},
            {"name": "Bob", "age": "25"},
        ],
        [
            {"city": "Paris", "year": "2023"},
            {"city": "Berlin", "year": "2024"},
        ],
    ],
)
def test_csv_to_json_basic(tmp_path, rows):
    src = tmp_path / "input.csv"
    dst = tmp_path / "output.json"

    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(src, dst)

    data = json.loads(dst.read_text(encoding="utf-8"))

    assert data == rows


@pytest.mark.parametrize(
    "content",
    [
        "",
        "a,b,c",
    ],
)
def test_csv_to_json_invalid_csv(tmp_path, content):
    src = tmp_path / "bad.csv"
    dst = tmp_path / "out.json"

    src.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(src, dst)


@pytest.mark.parametrize(
    "src_name, dst_name, error",
    [
        ("data.txt", "out.json", ValueError),
        ("data.csv", "out.txt", ValueError),
        ("missing.csv", "out.json", FileNotFoundError),
    ],
)
def test_csv_to_json_path_errors(tmp_path, src_name, dst_name, error):
    src = tmp_path / src_name
    dst = tmp_path / dst_name

    if src_name != "missing.csv":
        src.write_text("a,b\n1,2", encoding="utf-8")

    with pytest.raises(error):
        csv_to_json(src, dst)
