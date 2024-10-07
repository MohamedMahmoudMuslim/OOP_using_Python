'''
Polymorphism = Greek word that means to "have many forms of faces"
    Poly = Many 
    Morphe = Form

Two ways to achieve polymorphism:
    1- Inheritance = An object could be treated of the same type as a Parent calss
    2- "Duck typing" = Object must have necessary attributes/methods
'''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius**2
        
        

class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    def area(self):
        return 0.5*self.base*self.height
    
class Pizza(Circle):
    def __init__(self, radius):
        super().__init__(radius)

def main():
    shapes = [Circle(4), Square(5), Triangle(5,6), Pizza(4)]

    for shape in shapes:
        print(f"Area = {shape.area()}cm²")
main()        


