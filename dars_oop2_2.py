# class Hayvon:
#     def __init__(self, nom, mavjudlik, qizil_kitob):
#         self.nom = nom
#         self.mavjudlik = mavjudlik
#         self.qizil_kitob = qizil_kitob
#
#     @property
#     def yur(self):
#         return f"{self.nom} yuryapti"
#
# ot = Hayvon("saman", True, False)
# print(ot.qizil_kitob, type(ot.qizil_kitob))
# print(ot.yur())


# class Student:
#     course = 2
#     student_count = 0
#     def __init__(self, first_name, last_name, phone, age=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.__phone = phone
#         Student.student_count += 1
#
#     def get_phone(self):
#         return self.__phone
#
#     def update_phone(self, phone):
#         self.__phone = phone
#
#     @classmethod
#     def get_student_count(cls):
#         return cls.student_count
#
#     @classmethod
#     def update_course(cls, course):
#         cls.course = course
#
#
#
# student1 = Student("Lazizbek", 'Karimov', 901234567)
# student2 = Student("Abror", 'Majidov', 991234567)
# student3 = Student("Bahodir", 'Obloqulov', 991234567)
# student4 = Student("Daler", 'Norqulov', 991234567)
# print(student1.first_name)
# print(student1.get_phone())
# student1.update_phone(123456789)
# print(student1.get_phone())
# print(student1.course)
# print(student2.course)
# print(student1.student_count)
# print(Student.get_student_count())
# Student.update_course(3)
# print(student3.course)



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def vector_len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        return self.vector_len() < other.vector_len()



v1 = Vector(2,5)
v2 = Vector(3,6)
v3 = Vector(3,4)
print(v1)
print(v2)
print(v1 + v2)
print(v3.vector_len())
if v1 < v2:
    print(v2, "bu", v1, "dan katta")
else:
    print(v1, "bu", v2, "dan katta")