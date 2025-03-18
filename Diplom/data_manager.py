import json
import os
from person import Person

class DataManager:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        self.people = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Важлива перевірка на структуру даних
                if isinstance(data, list):
                    return [Person.from_dict(p) for p in data]
                else:
                    print("Помилка: Некоректний формат даних у файлі. Починаємо з порожнього списку.")
                    return []

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Помилка завантаження даних: {e}. Починаємо з порожнього списку.")
            return []


    def save_data(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([p.to_dict() for p in self.people], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Помилка збереження даних: {e}")

    def add_person(self, person):
        self.people.append(person)
        self.save_data()

    def search(self, query):
        query = query.lower()
        results = []
        for person in self.people:
            if (query in person.first_name.lower() or
                (person.last_name and query in person.last_name.lower()) or
                (person.patronymic and query in person.patronymic.lower())):
                results.append(person)
        return results

    def get_all_people(self):  # Додано метод для отримання всіх записів
        return self.people