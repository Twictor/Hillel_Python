from student import Student
from group import Group, StudentsLimitError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert gr.find_student('Jobs') == st1, "Test failed: st1 not found"
assert gr.find_student('Jobs2') is None, "Test failed: Non-existent student found"

gr.delete_student('Taylor')
print(gr)

try:
    for i in range(3, 12):
        gr.add_student(Student('Male', 20 + i, 'Name' + str(i), 'Surname' + str(i), 'AN' + str(140 + i)))
except StudentsLimitError as e:
    print(e)