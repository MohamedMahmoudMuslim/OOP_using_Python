'''
Duck typing = Another way to achieve polymorphism besides Inheritance 
              Object must have the minimum necessary attributes/methods
            " if it looks a duck and quacks like a duck, it must be a duck."
'''

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEWO!")


class Car:
    alive = False 
    def speak(self):
        print("HONK!")

def main():
# we here consider the Car() is an animal as it has the minimum attributes and methods of animals
    animals = [Dog(), Cat(), Car()]
    for animal in animals:
        animal.speak()
        print(animal.alive)
main()