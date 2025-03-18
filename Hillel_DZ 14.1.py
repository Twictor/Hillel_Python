class StudentsLimitError(Exception):
    def __init__(self, message="The group cannot have more than 10 students"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise StudentsLimitError()
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        students = self.find_student(last_name)
        if students:
            self.group.remove(students)

    def find_student(self, last_name):
        for students in self.group:
            if students.last_name == last_name:
                return students
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        all_students = all_students.rstrip('\n')
        return f'Number:{self.number}\n{all_students}'


# Приклад використання
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 23, 'Jane', 'Doe', 'AN147')
st5 = Student('Male', 24, 'Mike', 'Smith', 'AN148')
st6 = Student('Female', 25, 'Anna', 'Johnson', 'AN149')
st7 = Student('Male', 26, 'Bob', 'Brown', 'AN150')
st8 = Student('Female', 27, 'Alice', 'Davis', 'AN151')
st9 = Student('Male', 28, 'Charlie', 'Wilson', 'AN152')
st10 = Student('Female', 29, 'Diana', 'Evans', 'AN153')
st11 = Student('Male', 30, 'Ethan', 'Thompson', 'AN154')
st12 = Student('Male', 40, 'Jayson', 'Grin', 'AN184')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
    gr.add_student(st12)

except StudentsLimitError as e:
    print(e)
