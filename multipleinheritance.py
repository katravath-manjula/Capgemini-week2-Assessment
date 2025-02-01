# 9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        print("The car is moving on the road.")

class Airplane:
    def move(self):
        print("The airplane is flying in the sky.")

class FlyingCar(Car, Airplane):
    def move(self):
        super().move()
      
        print("The flying car is driving on the road and flying in the sky.")


flying_car = FlyingCar()
flying_car.move()  
