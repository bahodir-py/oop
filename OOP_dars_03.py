# # utilgan darsni takrorlash 
# #  3_dars polimorfizm
# # hodimning oyligini oshiramiz (foizda)
# class Employee:
#     emp_count  =  0
#     protcent = 0
#     def __init__(self,first_name,email,salary):
#         self.first_name = first_name
#         self.email = email
#         self.__salary = salary   # yopiq inkopsulyatsiya qildik
#         Employee.emp_count += 1

#     @property
#     def get_salary(self):
#         return self.__salary

#     def set_salary(self):
#         Employee.protcent  = int(input("Necha foizga oshirasiz : "))
#         self.__salary +=  self.__salary * (Employee.protcent)//100

# #name1 = str(input("inter a name1: "))
# #name2 = str(input("inter a name2: "))
# emp1 = Employee("Dostonjon","bahodir@fgmail,com",500)
# emp2 = Employee("Dilshod","Botirovr@fgmail,com",700)

# print(emp1.first_name)
# print(emp1.get_salary)
# emp1.set_salary()
# print(emp1.get_salary)
# print(emp2.first_name)
# print(emp2.get_salary)
# emp2.set_salary()
# print(emp2.get_salary)



# dars_3 , vorislik,, polimorfizm, obyekt ichida obyekt
class User:
    def __init__(self, username, email):  # super/ ota / parent klass
        self.username = username
        self.email = email

    def login(self):
        return f"{self.username} tizimga kirdi "  

    def logout(self):
        return f"{self.username} tizimdan chiqdi "


class Student(User): # vorislik
    def __init__(self, username, email, course):
        super().__init__(username, email)  # voris olish
        self.course = course

    def task_send(self):
        return f"{self.username} vazifalarni yukladi"


class Teacher(User): # vorislik
    def __init__(self, username, email, degree):
        super().__init__(username, email) # voris olish
        self.degree = degree

    def task_chack(self):
        return f"{self.username} vazifalarni tekshirdi "

st1 = Student("Oybek","Oybek@gmail.com",2)
print(st1.email)
teacher1 = Teacher("Bobur","Bobur@gmail.com","Middle")
print(teacher1.username)

# class Person:
#     def __init__(self) -> None:
#         pass
# 