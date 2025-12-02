from pathlib import Path
from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json


def main():
    input = Path("data/lab08/students_input.json")
    output = Path("data/lab08/students_output.json")
    students = students_from_json(input)
    students_to_json(students, output)

    for student in students:
        print(student, student.age())


if __name__ == "__main__":
    main()
