'''
from uuid import uuid4


class Student():
    __course = 1
    def __init__(self, first_name, last_name, age, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__phone = phone
        self.__id = uuid4()

    def get_id(self):
        return self.__id

    @property
    def get_phone(self):
        return self.__phone

    def update_phone(self, phone_number):
        self.__phone = phone_number

    @classmethod
    def get_course(cls):
        return cls.__course

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

student1 = Student("Ali", "Aliyev", 22, 901234567)
student2 = Student("Vali", "Valiyev", 20, 991234567)
student3 = Student("Vali", "Valiyev", 20, 991234567)

# print(student1.first_name)
# print(student1.last_name)
# print(student1.get_id())
# print(student1.get_phone)
# student1.update_phone(971234569)
# print(student1.get_phone)
# print(student1.get_course())
# print(student2.get_course())
# print(Student.get_course())

print(student3 == student2)
print(student1 == student2)

if student1 > student2:
    print(f"{student1} katta {student2} dan")

'''

class Vektor():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"vektor({self.x} {self.y})"

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

v1 = Vektor(2,3)
v2 = Vektor(4,7)

print(v1 + v2)