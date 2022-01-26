# dars 2   inkapsulyatsiya
from uuid import uuid1

class Student:
    """ student klasi """
    student_count = 0 # klas atribut
    __course = 1 # kals atribut
    def __init__(self,first_name,last_name,phone,age):   # instance atribut ,# obyekntning xusuyatlari ni inkapsulyatsiya qildik 
        self.first_name = first_name
        self.last_name = last_name
        self.__phone = phone
        self.age = age
        self.__id = uuid1()
        Student.student_count += 1  # sanagich bu klas ga tegishli shu sababli klas nomi bn boshlaymiz
    
    @property  # decarator
    def get_id(self):
        return self.__id

    @property # decarator
    def get_phone(self):
        return self.__phone

    @classmethod  # dekarator
    def get_course(cls):
        return cls.__course

    def __str__(self):  # dunder metod
        return self.first_name + ' ' + self.last_name

    def __gt__(self,other):  # dunder metod
        return self.age > other.age

    def __eq__(self,other):  # dunder metod
        return self.age == other.age

st1 = Student("Oybek","Sayfiyev","123456789",18)
st2 = Student("Bahodir","Obloqulov","213461634",18)
st3 = Student("Lazizbek","Karimov","1234554322",17)

# print(f"ID student1 : {st1.get_id} ")   
# print(st1.get_phone)
# print(f"ID student2 : {st2.get_id}")
# print(st2.get_phone)
#print(Student.student_count)
#print(st1.get_course())
#print(Student.get_phone)
#print(st1.get_phone)
#print(st1)

#from pprint import pprint # chiroyli chiqarish
# double underclass metodlar
# dunder metods
#print(st1)  # endi bu xatoni torilaymiz
#print(st1)
#print(st2)
#print(st3) # kamchilik torilandi
#pprint((dir(Student)))
#print(st1 == st3)
#print(st1 > st2)
if st1 == st2:
    print(f"{st1.first_name} yoshi {st2.first_name} yoshi bn teng")
if st1 > st3:
    print(f"{st1.first_name} yoshi {st3.first_name} yoshidan katta")



