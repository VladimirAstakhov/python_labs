import json
import csv
from pathlib import Path


def json_to_csv(json_path, csv_path):
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if json_path.suffix.lower() != ".json":
        raise ValueError("Неверный тип входного файла: нужен .json")

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Неверный тип выходного файла: нужен .csv")

    if not json_path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список объектов")

    fieldnames = list(data[0].keys())
    for item in data:
        row = {key: item.get(key, "") for key in fieldnames}
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path, json_path):
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Ожидается CSV-файл на входе")
    if json_path.suffix.lower() != ".json":
        raise ValueError("Ожидается JSON-файл на выходе")

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV пустой или без заголовка")

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
