# tekislik yuzasi
class Tekislik:
    def __init__(self,number):
        self.number = number

    def inputtomon(self):
        return [int(input("tomon uzunligini kiriting: " + str(i+1) + '- tomon: ')) for i in range(self.number)]

    def yuza(self):
        return 'Bu metod bizga yuzani hisoblab beradi! '

class Uchbuechak(Tekislik):
    
    def kirit(self):
        self.a, self.b, self.c = self.inputtomon()

    def yuza(self):
        if self.a + self.b > self.c   or   self.a + self.c > self.b   or   self.c + self.b > self.a:
            p = (self.a + self.b + self.c)/2
            s = (p*(p - self.a)*(p - self.b)*(p - self.c)) ** 0.5
            return s
        return f"Siz kiritgan tomonlardan uchburchak yasab bo`lmaydi!"

    def pr(self):
        return self.a + self.b + self.c
        
uchb = Uchbuechak(3)
uchb.inputtomon()
print(uchb.yuza())
print(uchb.pr())






