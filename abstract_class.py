'''
Abstract calss: A class that cannot be instantiated on its own; Meant to be subclassed.
They can contain abstract methods, which are declared but have no implementation.

Abstract classes benefits:
    1- Prevents instantiation of the class itself.
    2- Requires children to use inherited abstract methods
# the clildren only can modify the abstracted methods and make instances (objects) from it
'''
from abc import ABC, abstractmethod

# abstracted Parent class 
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Childs 
class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class MotorCycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print("You sail the Boat")
    
    def stop(self):
        print("You anchor the Boat")


# objects
car = Car()
motorcycle = MotorCycle()
boat = Boat()

#test the methods which child inherit from the abastract class 
car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

boat.go()
boat.stop()





