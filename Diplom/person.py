import re
import json
from datetime import datetime


class Person:
    DATE_FORMATS = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]

    def __init__(self, first_name, last_name=None, patronymic=None, birth_date=None, death_date=None, gender=None):
        if not first_name:
            raise ValueError("Ім'я є обов'язковим полем")

        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize() if last_name else None
        self.patronymic = patronymic.capitalize() if patronymic else None
        self.birth_date = self.parse_date(birth_date)

        # Проверяем, является ли переданный параметр death_date датой, а не полом
        if death_date and re.match(r"^\d{2}[-./]\d{2}[-./]\d{4}$", death_date):
            self.death_date = self.parse_date(death_date)
            self.gender = gender.lower() if gender in ["m", "f"] else None
        else:
            self.death_date = None
            self.gender = death_date.lower() if death_date in ["m",
                                                               "f"] else None  # Если нет даты смерти, значит это пол

    def parse_date(self, date_str):
        if not date_str:  # Если пустая строка или None, просто вернуть None
            return None
        for fmt in self.DATE_FORMATS:
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Невірний формат дати: {date_str}")

    def calculate_age(self):
        if not self.birth_date:
            return None
        end_date = self.death_date or datetime.today().date()
        return end_date.year - self.birth_date.year - (
                    (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "patronymic": self.patronymic,
            "birth_date": self.birth_date.strftime("%d.%m.%Y") if self.birth_date else None,
            "death_date": self.death_date.strftime("%d.%m.%Y") if self.death_date else None,
            "gender": self.gender
        }

    @staticmethod
    def from_dict(data):
        return Person(
            first_name=data["first_name"],
            last_name=data.get("last_name"),
            patronymic=data.get("patronymic"),
            birth_date=data.get("birth_date"),
            death_date=data.get("death_date") if "death_date" in data and data["death_date"] else None,
            gender=data.get("gender")
        )


