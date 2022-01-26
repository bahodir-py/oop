# # class   ->  Calculator
# from math import modf


# class Calc:

#     @staticmethod
#     def add(*n):
#         return sum(n)

#     @staticmethod
#     def sub(x,y):
#         if x > y:
#             return x - y 
#         else:
#             return y - x

#     @staticmethod
#     def prod1(*n):
#         from math import prod
#         return prod(n)
    
#     @staticmethod
#     def div(x,y):
#         if y!= 0:
#             return x / y 
#         else:
#             return f"nolga bulish mumkin emas"

#     @staticmethod
#     def modul(x):
#         if x >= 0:
#             return x
#         else:
#             return -x 
# c = Calc()
# print(Calc.add(1,2,3,4))  # agar  static metod   deb yozmasak unda  faqatgina clasdan murojda ishlaydi
# print(c.add(2,3,5,6)) # endi  bu static metod buldi
# print(c.sub(1,10)) # static  metod
# print(c.sub(23,4)) # static  metod
# print(c.prod1(1,2,3,4,5))
# print(c.div(12,0))
# print()
# print(c.modul(-4))
# print()
# print(c.modul(5))

class Math:

    @staticmethod
    def pow(x,y):
        return x ** y
    
    @staticmethod
    def abs(x):
        if x >= 0:
            return x
        else:
            return -x
    
    @staticmethod
    def sqrt(x):
        return x ** 0.5
    
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def sub(x,y):
        if x >=y  :
            return x - y
        else:
            return y - x

    @staticmethod
    def log(a,b):
        from math import log
        return log(b)/log(a)

    

num = Math()
print(Math.pow(4,2))
print(num.pow(2,5))
print(num.log(2,4))

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def vektor(self):
        return self.x,self.y
        
    @classmethod
    def vektor_len(cls,l,angle):
        from math import cos,sin 
        cls.x = l * cos(angle)
        cls.y = l * sin(angle)
        return cls.x,cls.y

# vektor1 = Vector(5,4)
# print(vektor1.vektor_len(5,2))
v1 = Vector(2,3)
print(v1.vektor())
print(v1.vektor_len(5,1))











