class Electronics:
    def __init__(self,name,brand):
        self.n=name
        self.b=brand
    def turnon(self):
        print(f"Electronic name : {self.n} ,brand {self.b}")


class Smartphone(Electronics):
    def __init__(self, name, brand,camera,):
        super().__init__(name, brand)
        self.cam=camera
    def turnon(self):
        super().turnon()
        print(f"Smartphone Name: {self.n}, Brand: {self.b}, Camera: {self.cam}MP")

phone = Smartphone("Samsung", "Galaxy S24", 108)

phone.turnon() 
        