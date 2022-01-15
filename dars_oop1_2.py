my_list = ["user1", "email" "user: user1 email: email"]

my_dict = {
    'user': "User1",
    'email': "Eamil",
    'about': "User: user1, Email: Email"
}

#
# class User:
#     def __init__(self, first_name, last_name, age, address=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def about(self):
#         return f"Mening I.F {self.full_name} yoshim: {self.age}"
#
#     def greet(self, user):
#         return f"{user.first_name}: Hi {self.full_name} "
# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class User:
#     first_name: str
#     last_name: str
#     age: int
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def about(self):
#         return f"Mening I.F {self.full_name} yoshim: {self.age}"
#
#     def greet(self, user):
#         return f"{user.first_name}: Hi {self.full_name} "
#
# user = User("Lazizbek", "Karimov", 19)
# user2 = User("Bahodir", "Obloqulov", 18)
#
# print(user.first_name)
# print(user.full_name)
# print(user.about)
#
# print(user2.first_name)
# print(user2.full_name)
# print(user2.about)
#
# print(user.greet(user2))
# print(user2.greet(user))


class Student():
    def __init__(self, first_name, course, group, faculty):
        self.first_name = first_name
        self.course = course
        self.group = group
        self.faculty = faculty

    def about(self):
        return f"{self.first_name} {self.course}, {self.group}"

student1 = Student("Lazizbek", 2, 203, "RT")
student2 = Student("Daler", 2, 203, "RT")
student3 = Student("Abror", 2, 203, "RT")
student4 = Student("Bahodir", 2, 203, "RT")
student5 = Student("Abduvohid", 2, 203, "RT")

class Subject():
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        return self.students.append(student)

    def  get_students(self):
        return [student.about() for student in self.students]


backend = Subject('Paython backend')
backend.add_student(student1)
backend.add_student(student2)
backend.add_student(student5)

print(backend.name)
for s in backend.get_students():
    print(s)

coding = Subject("Programming")
coding.add_student(student1)
coding.add_student(student2)
coding.add_student(student3)
coding.add_student(student4)
coding.add_student(student5)

print(coding.name)
for s in coding.get_students():
    print(s)