# Protsessor
# Ram
# Plata 
class Computer:
    def __init__(self ,color,protsessor,ram,platas):
        self.color = color
        self.protsessor = protsessor
        self.ram = ram
        self.platas = platas
    
    def get_about(self):
        return f'''
        rangi : {self.color},
        Protsessor : {self.protsessor.get_protsessor()}
        RAM : {self.ram.get_ram()}  {self.platas.get_plata()}
        '''

class Protsessor:
    def __init__(self,model,versiya,chastota):
        self.model = model
        self.versiya  = versiya
        self.chastota = chastota
    
    def get_protsessor(self):
        return f''' 
        Turi : {self.model}, avlodi : {self.versiya}, 
        chastotasi {self.chastota}
        '''

class Ram:
    def __init__(self,operativ_xotira,doimiy_xotira):
        self.operativ_xotira = operativ_xotira
        self.doimiy_xotira = doimiy_xotira

    def get_ram(self):
        return f'''
        operativkasi : {self.operativ_xotira}, 
        doimiy xotirasi : {self.doimiy_xotira}
        '''

class Plata:
    def __init__(self,plata,razryad):
        self.plata = plata
        self.razryad = razryad

    def get_plata(self):
        return f'''
        platasi : {self.plata},
        Razryadi : {self.razryad}
        '''


protsessor1 = Protsessor('HP','9','4.8 Hz')
ram1 = Ram(8.00,700)
plata1 = Plata('platasi',64)
comp1 = Computer('gray',protsessor1,ram1,plata1)

protsessor2 = Protsessor('Acer','12','8.6 Hz')
ram2 = Ram(16.00,518)
plata2 = Plata('platasi',32,)
comp2 = Computer('black',protsessor2,ram2,plata2)

protsessor3 = Protsessor('Lenovo','10','3.2 Hz')
ram3 = Ram(4.00,711)
plata3 = Plata('platasi',64)
comp3 = Computer('white',protsessor3,ram3,plata3)

print('1-si')
print(comp1.get_about())
# print(comp1.ram.get_ram())
# print(comp1.platas.get_plata())
print('2-si')
print(comp2.get_about())
# print(comp2.ram.get_ram())
# print(comp2.platas.get_plata())
print('3-si')
print(comp3.get_about())
# print(comp3.ram.get_ram())
# print(comp3.platas.get_plata())








