'''
multiple inheritance = inherit from more than one parent calss  
    class Parent1(self):
    class Parent2(self):
    class Child(Parent1, Parent2):
    
multi-level inheritance = inherit from parent which inherits from grand-parent and, so on.....
    class GrandParent(self):
    class Parent(GrandParent):
    class Child (Parent):
'''
#GrandParents
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

#Parnets
class Prey(Animal):
    def flee (self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt (self):
        print(f"{self.name} is hunting") 

#Childs
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass 
class Fish(Prey, Predator):     # multiple inheritance
    pass 

def main():
    rabbit = Rabbit("Bugs")
    hawk = Hawk("Tony")
    fish = Fish("Nemo")

    fish.hunt()
    fish.flee()
    print(fish.name)

    rabbit.eat()
main()