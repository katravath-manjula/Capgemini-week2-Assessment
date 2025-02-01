from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(f"Area of Rectangle: {self.length * self.width}")

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")

rectangle = Rectangle(5, 3)
circle = Circle(4)

rectangle.calculate_area()
circle.calculate_area()
