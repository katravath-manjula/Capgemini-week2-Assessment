#  Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Dog is barking")

class Cat(Animal):
    def speak(self):
        print("Cat is saying meow!")

def animal_sound(animal):
    animal.speak()  


dog = Dog()
cat = Cat()

animal_sound(dog) 
animal_sound(cat)  
