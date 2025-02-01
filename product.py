# 5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
    def __init__(self, name, price, stock):
        self.n = name
        self.p = price
        self.s = stock
        print(f"product name : {self.n} \n price: {self.p} \n stock : {self.s}")

    def check_availability(self, quantity):
        if quantity <= self.s:
            print("quantity is available")
        else:
            print("quantity is not available !")

product = Product("Laptop", 50000, 10)
product.check_availability(20)  
product.check_availability(5) 
product.check_availability(23)