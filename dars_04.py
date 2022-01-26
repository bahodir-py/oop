# 4-dars   OOP yakuni
# clasda pbyekt qaytarish
# manzil abyektini qaytarish
class Person:
    def __init__(self,first_name,last_name,age,address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.addrees = address

    def about(self):
        return f'''
        Ismi {self.first_name}, Familiyasi {self.last_name},
        Yoshi {self.age} da  
        manzili  : {self.addrees.get_address()}
        '''
    
class Address: # klass
    def __init__(self,region,district,street,heigborhod,home):
        self.region = region
        self.district = district 
        self.street = street 
        self.heigborhod = heigborhod
        self.home = home

    def get_address(self):
        return f'''
        {self.region} viloyati ,   {self.district} tumani ,
        {self.heigborhod}   MFY,   {self.street} ko`chasi,   {self.home} uy 
        '''

address2 = Address('Samarkand','Samarkand','K.Begzod','M.Ulug`bek','48/19')
address1 = Address('Samarkand','Samarkand','K. Begzod','A. Yassaviy','50/17')
person1 = Person('Bahodir','Obloqulov',18,address1)
person2 = Person('Shakhzod','Massaridinov',18,address2)

print(person1.about())
print(person1.addrees.get_address())
#print(address.get_address())
print()
print(person2.about())
print(person2.addrees.get_address())












