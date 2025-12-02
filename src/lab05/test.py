if __name__ == "__main__":
    from src.lab05.csv_xlsx import csv_to_xlsx
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from pathlib import Path

    BASE = Path(__file__).resolve().parents[2]

    INPUT_JSON = BASE / "data" / "samples" / "people.json"
    OUTPUT_CSV = BASE / "data" / "out" / "people_from_json.csv"

    INPUT_CSV = BASE / "data" / "samples" / "people.csv"
    OUTPUT_JSON = BASE / "data" / "out" / "people_from_csv.json"

    INPUT_CSV_2 = BASE / "data" / "samples" / "cities.csv"
    OUTPUT_XLSX = BASE / "data" / "out" / "people.xlsx"

    json_to_csv(INPUT_JSON, OUTPUT_CSV)
    csv_to_json(INPUT_CSV, OUTPUT_JSON)
    csv_to_xlsx(INPUT_CSV_2, OUTPUT_XLSX)
