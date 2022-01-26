'''
stek bushligi
element qushish
birinchi elementini chiqarish
oxirgi elementini chiqarish
nechta elemnti borligini ciqarish
'''
# stack - Last int - First out
# evrika!           ->     Bahodir
class Stack:
    def __init__(self,element):
        self.element = element
        self.stack = []

    def push(self,element):
        self.element = element
        self.stack.append(self.element)
        return f"element qushildi : {self.stack}, "

    def pop(self):
        return f"element uchirildi : {self.stack.pop()}, "

    def top(self):
        return f"eng yuqori elementi : {self.stack[-1]},"

    def size(self):
        return f"elementlarining soni : {len(self.stack)} ta ,"

    def empty(self):
        if self.stack == []:
            return f"stack bo'sh {self.stack}"
        else:
            return f"stack bo'sh emas , uning elementlari : {self.stack}"

elem1 = Stack(2)
elem1.push(1)
elem1.push(2)
elem1.push(3)
elem1.push(4)
elem1.push(5)
elem1.push(6)
elem1.push(7)
elem1.push(8)
elem1.push(9)
elem1.push(10)

print(elem1.size())
print(f"{elem1.stack}")
print(elem1.pop())
print(elem1.size())
print(f"{elem1.stack}")
print(elem1.top())

print(elem1.empty())
print(elem1.size())
print(f"{elem1.stack}")
print(elem1.push(112))
print(elem1.size())
print(f"{elem1.stack}")

