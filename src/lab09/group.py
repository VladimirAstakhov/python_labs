import csv
from pathlib import Path
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def _read_all(self):
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["gpa"] = float(row["gpa"])
                rows.append(row)
        return rows

    def list(self):
        rows = self._read_all()
        return [Student.from_dict(r) for r in rows]

    def add(self, student: Student):
        file_empty = self.path.stat().st_size == 0
        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            if file_empty:
                f.write("fio,birthdate,group,gpa\n")
            writer.writerow(student.to_dict())

    def find(self, substr: str):
        rows = self._read_all()
        return [r for r in rows if substr in r["fio"]]

    def remove(self, fio: str):
        rows = self._read_all()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break

        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)

    def update(self, fio: str, **fields):
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for key, value in fields.items():
                    if key in r:
                        r[key] = value
                break

        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
