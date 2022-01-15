#
# class Employee:
#     emp_count = 0
#     procent = 0
#     def __init__(self, first_name, email, salary):
#         self.first_name = first_name
#         self.emial = email
#         self.__salary = salary
#         Employee.emp_count += 1
#
#     @property
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self):
#         Employee.procent = int(input('Necha foizga oshirmoqchisiz: '))
#         self.__salary += self.__salary * (Employee.procent)//100
#
#
#
# emp1 = Employee('Oybek', 'oybek@gmail.com', 500)
# emp2 = Employee('Sherdil', 'sherdil@gmail.com', 500)
# print(emp1.get_salary)
# emp1.set_salary()
# emp2.set_salary()
# print(emp1.get_salary)
# print(emp2.get_salary)
#

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        return f'{self.username} tizimga kirdi'

    def logout(self):
        return f'{self.username} tizimdan chiqdi'

class Student(User):
    def __init__(self, username, email, course):
        super().__init__(username,email)
        self.course = course

    def task_send(self):
        return f'{self.username} vazifani yubordi'

class Teacher(User):
    def __init__(self, username, email, degree):
        super().__init__(username, email)
        self.degree = degree

    def task_check(self):
        return f'{self.username} vazifalarni tekshirdi'

# st1 = Student('obyek', 'oybek@gmail.com', 2)
# print(st1.email)
# teacher1 = Teacher('bobur', 'bobur@gmail.com', 'middle')
# print(teacher1.username)


class Person:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def get_about(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.address

class Employee(Person):
    def __init__(self, first_name, last_name, address, job):
        super().__init__(first_name, last_name, address)
        self.job = job

    def get_about(self):
        return f'{self.first_name} {self.last_name} {self.address} {self.job}'

person1 = Person('Ali', 'Valiyev', 'Samarqand')
print(person1.get_about())

emp1 = Employee('Valijon', 'Valiyev', 'Samarqand', 'developer')
print(emp1.get_about())