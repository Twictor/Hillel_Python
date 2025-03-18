import json
import os
from person import Person

class DataManager:
    FILE_PATH = "data.json"

    def __init__(self):
        self.people = self.load_data()

    def load_data(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as file:
            return [Person.from_dict(p) for p in json.load(file)]

    def save_data(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([p.to_dict() for p in self.people], file, ensure_ascii=False, indent=4)

    def add_person(self, person):
        self.people.append(person)
        self.save_data()

    def search(self, query):
        query = query.lower()
        return [p for p in self.people if query in p.first_name.lower() or
                (p.last_name and query in p.last_name.lower()) or
                (p.patronymic and query in p.patronymic.lower())]
