# 18. Implement an abstract class `ICalculator` with methods ``, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def __init__(self, a, b):  
        self.a = a
        self.b = b

    def add(self):
        print(f"Addition: {self.a} + {self.b} = {self.a + self.b}")

    def subtract(self):
        print(f"Subtraction: {self.a} - {self.b} = {self.a - self.b}")

    def multiply(self):
        print(f"Multiplication: {self.a} × {self.b} = {self.a * self.b}")

    def divide(self):
        if self.b != 0:
            print(f"Division: {self.a} ÷ {self.b} = {self.a / self.b}")
        else:
            print("Error: Division by zero is not allowed.")


ob = BasicCalculator(4, 2)
ob.add()
ob.subtract()
ob.multiply()
ob.divide()
