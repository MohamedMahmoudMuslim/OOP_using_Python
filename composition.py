'''
Composition = The comoposed object directly owns its components, which cannot exist independently 
              "owns-a" relationship
'''

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power 

class Wheel:
    def __init__(self, size):
        self.size = size

# composite class which owns attributes as objects of other classes 
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make 
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def describe(self):
        return f"{self.make} {self.model},its engine power is {self.engine.horse_power}(hp) with wheel size {self.wheels[0].size} inches"


def main():
    car1 = Car("Ford", "Mustang", 600, 20)
    print(car1.describe())

main()