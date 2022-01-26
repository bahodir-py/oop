#  sudent -> usename, email, passvord :::    + yunalish  + kurs
# teacher ->  <> + mutahasslik + daraja
class User:
    def __init__(self,username,email,password):
        self.username =  username
        self.email = email
        self.password = password

    @property # decarator
    def login(self):
        return f"{self.username} l o g i n"

    @property  # decarator
    def logout(self):
        return f"{self.username} log O U T"


class Student(User):
    def __init__(self,username,email,password,direction,course):
        super().__init__(username,email,password)
        self.direction = direction
        self.course = course

    def send_task(self):
        return f"{self.username} sending homeworks"

    def read_task(self):
        return f"{self.username} reading homeworks"

class Teacher(User):
    def __init__(self, username, email, password,specialization,degree):
        super().__init__(username, email, password)
        self.specialization = specialization
        self.degree = degree

    def task_check(self):
        return f"{self.username} is cheking task"

    def specialization_is(self):
        return f"{self.username} 's specialization {self.specialization}"

    def degree_is(self):
        return f"{self.username} 's degree {self.degree}"

us1 = User("Akmal","Akmal@gmail.com","********")
us2 = User("Anvar","AnvarNarzullayev@gmail.com","***************")

st1 = Student("B_Dev","B_dev_senior","*********","M. analiz asoslari",1)
st2 = Student("Nikname","Nikname@mail.ru","***####****","K algebrasi",3)

tech1 = Teacher("ObloqulovB_Dev","B_py.mail.ru","##**##**##**","Mentor1","middle")
tech2 = Teacher("Shokirov","Nuriddinoffical#","****###**##*#*#*#*##*#**#","mentor2","senior")
print(us1.username)
print(us1.login)
print(us1.logout)

print(us2.login)
print(us2.logout)
print(st1.username)
print(st2.read_task())

print(tech1.username)
print(us2.login)
print(us2.logout)
print(tech1.task_check())