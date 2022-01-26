# Kompyuter nomli model, rang, chastota, RAM, SSD, HDD 
# xususiyatlarga va ishga_tush(),
#  ishni_yakunla(), faylni_och(), malumot_ber() 
# nomli metodlarga ega obyekt yarating.
#  Uning namunalarini yarating

class Kompyuter:
    def __init__(self,model,rang,chastota,RAM,SSD,HDD):
        self.model = model
        self.rang = rang
        self.chastota = chastota
        self.RAM = RAM
        self.SSD = SSD
        self.HDD = HDD

    def ishni_yakunla(self):
        return f"{self.model} ishni yuklamoqda"

    def faylni_och(self):
        return f"{self.model} faylni ochmoqda"

    def about(self): # metod malumot beruvchi
        return f'''
        modeli {self.model}
        Rangi {self.rang} 
        chastota {self.chastota}
        RAM {self.RAM}
        SSD  {self.SSD}
        HDD {self.HDD}
        '''
    def update_model(self,model):
        self.model = model


komp1 = Kompyuter('Lenovo','white',2,4,8,9)
komp1.update_model('ACER')


kopm2 = Kompyuter('Hp','black',4,8,8,16)

print(komp1.ishni_yakunla())
print(kopm2.faylni_och())
print(komp1.about())
print(kopm2.about())