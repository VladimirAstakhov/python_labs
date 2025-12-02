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
        fio="Тест Тестов",
        birthdate="2025-01-01",
        group="БИВТ-25-2",
        gpa=5.0
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
