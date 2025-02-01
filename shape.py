# Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def _init_(self):
        pass

class Square(Shape):
    def __init__(self, sides):
        super().__init__()
        self.s = sides
    
    def area(self):
        print(f"Area of Square: {self.s * self.s}")

class Triangle(Shape):
    def __init__(self, base, height):
        super()._init_()
        self.b = base
        self.h = height
    
    def area(self):
        print(f"Area of Triangle: {0.5 * self.b * self.h}")

square = Square(4)
triangle = Triangle(5, 6)

square.area()  
triangle.area()