# Hayvon nomli nom, mavjudlik(True yoki False), qizil_kitob(True yoki False)
# xususiyatlariga va yur(), yugur(), sakra(), ovoz_chiqar(), malumot_ber()
# metodlariga ega bo’lgan obyekt yarating. Ularning namunalarini yarating.

class Animal:
    def __init__(self,nom,mavjudlik,qizil_kitob,):# instance atribute yani xususiyatlari
        self.nom = nom
        self.mavjudlik = mavjudlik
        self.qizil_kitob = qizil_kitob
    
    @property # metodlarni qavssiz yozish uchun kk
    def yur(self):
        return f"{self.nom} yurayapti"
    
    @property
    def yugur(self):
        return f"{self.nom} yugurmoqda"
    
    @property
    def sakra(self):
        return f"{self.nom} sakrayapti"
    
    @property
    def ovoz_chiqar(self):
        return f"{self.nom} ovoz chiqarmoqda"
    
    @property
    def about(self):
        return f'''
        nomi : {self.nom}
        mavjudlik : {self.mavjudlik}
        qizil_kitob : {self.qizil_kitob}
        
        '''

animal1 = Animal('Kiyik','yes','yes')
animal2 = Animal('Silovsin','yes','no')
print(animal2.sakra)
print(animal2.yur)
print(animal2.yugur)
print(animal1.about)

