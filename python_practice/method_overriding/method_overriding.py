class Rectangle:
    def __init__(self):
        print('Inside init of Rectangle')
    def area(self,x):
        return x * x
    
class Square:
    pass

ob = Square(6)
print(ob.area(6))