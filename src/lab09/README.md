# Лабораторная работа №9 по Python

## «База данных» на CSV: класс Group, CRUD-операции и CLI

## Задание A - класс Group

```python
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

```

## Входные данные - data/lab09/students.csv

[students.csv](https://github.com/user-attachments/files/24208740/students.csv)

``` 
fio,birthdate,group,gpa
Иванов Иван,2003-10-10,БИВТ-21-1,4.3
Петрова Анна,2004-02-14,БИВТ-21-1,4.7
Сидоров Максим,2003-07-22,ПИ-22-2,3.9
Кузнецова Мария,2004-11-05,ПИ-22-2,4.5
Васильев Дмитрий,2003-03-30,ИСТ-21-3,4.1
Смирнова Ольга,2004-06-18,ИСТ-21-3,4.8
Фёдоров Алексей,2003-09-27,БИВТ-21-2,3.7
Морозова Елена,2004-01-09,БИВТ-21-2,4.6
```

## Скрипт тестирования - src/lab09/test.py

```python
from pathlib import Path
from group import Group
from src.lab08.models import Student


def main():
    project_root = Path(__file__).resolve().parents[2]
    csv_path = project_root / "data" / "lab09" / "students.csv"

    group = Group(csv_path)
    print("test read_all:")
    for element in group._read_all():
        print(element)

    print("test list:")
    for element in group.list():
        print(element)

    print("\ntest add:")
    new_student = Student(
        fio="Тест Тестов", birthdate="2025-01-01", group="БИВТ-25-2", gpa=5.0
    )
    group.add(new_student)

    for element in group.list():
        print(element)

    print("\ntest find (подстрока='Тест'):")
    found = group.find("Тест")
    for element in found:
        print(element)

    print("\ntest update (Изменяем группу и gpa):")
    group.update("Тест Тестов", group="ТЕСТ-ИЗМЕНЁН", gpa=4.9)

    for element in group.list():
        print(element)

    print("\ntest remove ('Тест Тестов'):")
    group.remove("Тест Тестов")

    for element in group.list():
        print(element)


if __name__ == "__main__":
    main()

```
## Результаты

## test add

<img width="524" height="290" alt="test add" src="https://github.com/user-attachments/assets/23b8db1f-9082-485f-b197-10e68920dac1" />

## test delete

<img width="537" height="263" alt="test delete" src="https://github.com/user-attachments/assets/ce4b0bc9-e488-4bfc-9be7-3c25ef2aa5e8" />

## test find

<img width="894" height="369" alt="test find" src="https://github.com/user-attachments/assets/734601ad-c8df-446f-ba8c-39951addd6d0" />

## test list

<img width="508" height="264" alt="test list" src="https://github.com/user-attachments/assets/b798c7d3-3808-4196-b315-56f8b2a3da4a" />

## test read_all

<img width="1036" height="259" alt="test read_all" src="https://github.com/user-attachments/assets/7f054dd7-ac82-4f00-af29-797dfc5becbf" />



