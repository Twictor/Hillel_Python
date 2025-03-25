import datetime
from datetime import datetime


class Person:
    DATE_FORMATS = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]

    def __init__(self, first_name, last_name=None, patronymic=None, birth_date=None, death_date=None, gender=None):
        if not first_name:
            raise ValueError("Ім'я є обов'язковим полем")

        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize() if last_name else None
        self.patronymic = patronymic.strip().capitalize() if patronymic else None
        self.birth_date = self._parse_date(birth_date)
        self.death_date = self._parse_date(death_date)
        self.gender = self._validate_gender(gender)

    def _parse_date(self, date_str):
        if not date_str:
            return None
        last_error = None
        for fmt in self.DATE_FORMATS:
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError as e:
                last_error = e
        raise ValueError(f"Невірний формат або неіснуюча дата: {date_str}. "
                         f"Спробуйте формати: дд.мм.рррр, дд мм рррр, дд/мм/рррр, дд-мм-рррр") from last_error

    def _validate_gender(self, gender):
        if gender is None: return None
        gender = gender.lower()
        if gender in ["m", "f", "ч", "ж", "male", "female", "man", "woman"]:
            return "m" if gender in ["m", "ч", "male", "man"] else "f"
        raise ValueError("Невірна стать. Вкажіть 'm', 'f', 'ч', 'ж', 'male', 'female', 'man' або 'woman'.")

    def calculate_age(self):
        if not self.birth_date:
            return None
        end_date = self.death_date or datetime.now().date()
        age = end_date.year - self.birth_date.year - (
                (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "patronymic": self.patronymic,
            "birth_date": self.birth_date.strftime("%d.%m.%Y") if self.birth_date else None,
            "death_date": self.death_date.strftime("%d.%m.%Y") if self.death_date else None,
            "gender": self.gender
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            last_name=data.get("last_name"),
            patronymic=data.get("patronymic"),
            birth_date=data.get("birth_date"),
            death_date=data.get("death_date"),
            gender=data.get("gender")
        )

    def __str__(self):
        parts = [self.first_name]
        if self.last_name:
            parts.append(self.last_name)
        if self.patronymic:
            parts.append(self.patronymic)

        age = self.calculate_age()
        age_str = f"{age} років" if age is not None else "вік невідомий"
        gender_str = {"m": "чоловік", "f": "жінка"}.get(self.gender, "стать не вказана")

        if self.gender == "f":
            birth_label = "Народилася"
            death_label = "Померла"
        else:
            birth_label = "Народився"
            death_label = "Помер"

        birth_date_str = f"{birth_label}: {self.birth_date.strftime('%d.%m.%Y')}" if self.birth_date else ""
        death_date_str = f"{death_label}: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ""

        return f"{' '.join(parts)}, {age_str}, {gender_str}. {birth_date_str}. {death_date_str}."
