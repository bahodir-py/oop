# vorislik
class Person:
    def __init__(self, first_name,last_name,address):  # super/ ota / parent klass
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    
    def get_about(self):
        return f"{self.first_name} {self.last_name} ning manzili : {self.address}"


class Employee(Person):
    def __init__(self, first_name,last_name,address,job): 
        super().__init__(first_name, last_name,address)  # voris olish
        self.job = job

    def get_about(self):  # polimorfizm degani shu
        return f"{self.first_name} {self.last_name} manzili : {self.address} , u {self.job}  bulib ishlaydi"
    #def get_about_employee(self):
     #   return f"{self.first_name} {self.last_name} manzili : {self.address} {self.job}  bulib ishlaydi"


pesron1 = Person("Bahodir","Obloqulov","Samarkand") 
print(pesron1.get_about())

emp1 = Employee("Lazizbek","Karimov","Tashkent","Backend_Dev")
print(emp1.get_about())


