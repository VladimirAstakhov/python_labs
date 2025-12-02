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
