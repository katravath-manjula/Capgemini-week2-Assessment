#Develop an interface IVehicle with abstract methods start_engine() and stop_engine(). Implement it in Car, Bike, and Truck classes.
from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        print("Car engine is started.")

    def stop_engine(self):
        print("Car engine is stopped.")


class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine is started.")

    def stop_engine(self):
        print("Bike engine is stopped.")


class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine is started.")

    def stop_engine(self):
        print("Truck engine is stopped.")


print("Truck Details:")
truck = Truck()
truck.start_engine()
truck.stop_engine()

print("\nBike Details:")
bike = Bike()
bike.start_engine()
bike.stop_engine()

print("\nCar Details:")
car = Car()
car.start_engine()
car.stop_engine()
