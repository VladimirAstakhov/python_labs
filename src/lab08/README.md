# Лабораторная работа №1 по Python

## ООП в Python: @dataclass Student, методы и сериализация

## Задание A - class Students

```python
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты рождения")

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должно быть от 0 до 5")

    def age(self) -> int:
        student_birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        now_date = datetime.today()
        age = now_date.year - student_birthdate.year
        if now_date.month < student_birthdate.month:
            age -= 1
        elif (
            now_date.month == student_birthdate.month
            and now_date.day < student_birthdate.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        student = Student(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

        return student

    def __str__(self):
        return f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"
```

```
Класс Student

A) Класс представляет информацию о студенте и включает поля:

1) fio — ФИО студента

2) birthdate — дата рождения в формате YYYY-MM-DD

3) group — учебная группа

4) gpa — средний балл (от 0 до 5)


B) При создании объекта выполняется проверка:

1) корректности формата даты рождения

2) допустимости значения GPA


C) Методы:

1) age() — вычисляет текущий возраст студента

2) to_dict() — возвращает данные студента в виде словаря

3) from_dict() — создаёт объект Student из словаря

4) __str__() — строковое представление студента
```

## Задание B - serialize.py

```python
import json
from .models import Student
from pathlib import Path


def students_to_json(students: list[Student], path: str | Path):
    data = [s.to_dict() for s in students]
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("В JSON должен лежать список студентов")
    students = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Информация о студенте должна храниться как словарь")
        student = Student.from_dict(item)
        students.append(student)
    return students

```

## students_input.json (входные данные):

<img width="809" height="943" alt="students_input json" src="https://github.com/user-attachments/assets/7e0e0522-46d1-4b51-9dc3-40e47464c205" />

## students_input.json (выходные данные после сериализации):

<img width="704" height="905" alt="students_output json" src="https://github.com/user-attachments/assets/260988ac-8588-4fbd-90c3-a13c6e906461" />


## тест  __post_init__:

``` 
У одного из студентов был введен gpa = 10, в students_input.json
```
<img width="1049" height="112" alt="проверка __post_init__" src="https://github.com/user-attachments/assets/28f0bc64-555d-45a2-8690-391017555115" />


## тест  age:

<img width="812" height="230" alt="проверка age" src="https://github.com/user-attachments/assets/1d4ea603-644a-4a11-a897-f9bf9eb5540f" />



