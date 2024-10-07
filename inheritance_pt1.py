#Inheritance = Allows a class to inherit attributes and methods from another class 
#              Helps with code reusability and extensibility
#              class Child (Parent):

class Animal: # Parent Class (Super Class)
    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# making some childs (SubClasses) form the Parent (SuperClass)
class Cat (Animal):
    def speak(self):
        print("MEOW!") 

class Dog (Animal):
    def speak(slef):
        print("WOOF!") 

class Mouse (Animal):
    def speak(self):
        print ("SQUEEK!") 

def main():
    # making some objects from the ChildClass 
    dog = Dog ("Scoby")
    cat = Cat ("Garfield")
    mouse = Mouse ("Mickey")

    # the following attributes and methods are shared for all Childs
    print(dog.name)
    print(cat.name)
    print(mouse.name)
    print(dog.is_alive)
    dog.eat()
    dog.sleep()

    # the following methods differ from Child to another
    dog.speak()
    cat.speak()
    mouse.speak()
main()