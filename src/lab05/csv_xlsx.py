
from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path, xlsx_path):
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Ожидается CSV-файл на входе")
    if xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается XLSX-файл на выходе")

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    widths = {}

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            ws.append(row)

            for i, cell in enumerate(row):
                length = len(str(cell))
                widths[i] = max(widths.get(i, 8), length)

    for i, w in widths.items():
        col_letter = ws.cell(row=1, column=i+1).column_letter
        ws.column_dimensions[col_letter].width = w + 2

    wb.save(xlsx_path)

