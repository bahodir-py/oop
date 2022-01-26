# 1-topshiriq
# vectorlar bn ishlash
class Vector:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

# double underclass metodlar
# dunder metods

    def __str__(self) -> str:  # dunder metod
        return f"Vector is ({self.x},{self.y})"

    def __add__(self,other):# dunder metod
        self.x1 = self.x +other.x
        self.y1 = self.y +other.y
        return f"ADDvectors  : ({self.x1},{self.y1})"
    
    def __sub__(self,other):
        self.x1 = self.x - other.x
        self.y1 = self.y - other.y
        return f"SUBvectors  : ({self.x1},{self.y1})"

    
    def length(self):
        return (self.x ** 2 + self.y ** 2 ) ** 0.5
    
    
    def __lt__(self, other):
        return self.length() < other.length()
 #   def __gt__(self,A.length,B.length):
  #      if self.{A.length} > self.{B.length}:

   #         return f"{A.length} katta {B.length} dan"
    #    else:
     #       return f"katta emas" 
     # ishlamadi

v1 = Vector(1,1)
v2 = Vector(2,2)
print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v2 - v1)

if v1 < v2 :
    print(v2, "katta ", v1 ,"vektordan ")
else:
    print(v1, "katta ", v2, "vektordan")
#print(v1.length > v2.length)






