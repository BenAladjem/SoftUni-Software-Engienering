from project.person import Person
from project.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


# t = Teacher()
# print(t.sleep())
# print(t.teach())
# print(t.get_fired())