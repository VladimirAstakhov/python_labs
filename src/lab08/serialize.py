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
