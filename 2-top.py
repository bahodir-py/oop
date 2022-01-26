# 2-topshiriq
# nom, rang , yosh
#  yurish, ovqatlanish, miyovlash,ma'lumot berish


class Cat: # klass nomi
    def __init__(self,name,color,age): # istance atribut
        self.name = name # xususiyatlar
        self.color = color
        self.age = color

    def yurish(self):# metod
        return f"{self.name} yurayapti"

    def ovqatlanish(self):# metod
        return f"{self.name} sut ichayapti"

    def miyovlash(self):#metod
        return f"{self.name} miyovlamoqda" 

    def about(self):#metod
        return f"{self.name} mushukning nomi, {self.color} mushukning rangi " 

cat1 = Cat("mosh","white",2) # uzgaruvchilar
cat2 = Cat("mitti","yellow",3)
cat3 = Cat("Kisula","Black",1)

print(cat1.miyovlash())
print(cat2.about())
print(cat3.ovqatlanish())



