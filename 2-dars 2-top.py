# ishchi nomli clas yarating,
# ismi. familiyasi. yoshi .oyligi kabi maydonlari bulsin
# get_id,     get_salary ,     set_salary   ka'bi metodlari bulsin
from uuid import uuid4
class Employee:
    ''' hodim klassi '''
    Emp_counter = 0
    def __init__(self,first_name,last_name,age,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__salary = salary  # maxfiy boldi
        self.__id = uuid4()  # maxfiy boldi
        Employee.Emp_counter += 1

    @property   # decarator  " end  qavs shartmas "
    def get_id(self):  # metod
        return self.__id

    @property # decarator
    def __str__(self): # dunder metod
        return  self.first_name + ' ' + self.last_name
    
    

    def __gt__(self,other):  # dunder metod
        return self.age > other.age # kattalikka  tekshirirish
    
    def __lt__(self,other):  # dunder metod
        return self.age < other.age  #  kichiklikka tekshirirish
    
    def __ne__(self,other):  # dunder metod
        return self.age != other.age  # teng emaslikka tekshirirish
    
    def __eq__(self,other):  # dunder metod
        return self.age == other.age  # tenglikka tekshirirish

    @property # decarator
    def get_salary(self):  # yuborilgan oylikni qayaradi
        return self.__salary  # maxfiy lik faqat employe isataganlarga kurinadi(faqat,oyigi)
    
    # @property  # decarator
    # def set_salary(self,salary):
    #     return self.__salary  #oylik yuboriladi
  
    @property  # decarator
    def get_id(self):
        return self.__id  
s1 = str(input("1-hodimning oyligini kirting: ($):"))
s2 = str(input("2-hodimning oyligini kirting: ($):"))
#s3 = str(input("3-hodimning oyligini kirting: ($):"))
#s4 = str(input("4-hodimning oyligini kirting: ($):"))

emp1 = Employee("Dostonbek","Ubaydullayev",25,s1)
emp2 = Employee("Shaxzod","Shodmonov",25,s2)
emp3 = Employee("Jasur","Mavlonov",28,"600000$")
emp4 = Employee("Bahodir","Obloqulov",18,"400$")


print(emp1.__str__)
print(emp1.get_id)
print(emp1.get_salary)

print()
print(emp2.__str__)
print(emp2.get_id)
print(emp2.get_salary)

print()
print(emp3.__str__)
print(emp3.get_id)
print(emp3.get_salary)

print()
print(emp4.__str__)
print(emp4.get_id)
print(emp4.get_salary)

# lkn setterni ishlatolmadim
if emp1 == emp2:
    print(f"{emp1.first_name} yoshi {emp2.first_name} yoshi bn teng")
#if emp3 > emp4:
 #   print(f"{emp3.first_name} yoshi {emp4.first_name} yoshidan katta")
if emp2 < emp3:
    print(f"{emp2.first_name} yoshi {emp3.first_name} yoshi bn teng")
if emp2 != emp3:
    print(f"{emp2.first_name} yoshi {emp3.first_name} yoshi bn teng emas")






