'''from the convention perspective:
    - the first letter of ecah word in name of the class 
      should be capitalized 
    - it's also should be meaningful 
    i.e.
    class Car:

    or 
    class ModleBased:  
'''


class Car: 
    def __init__(self, model, year ,color ,for_sale):     #dunder method (constructor)
        self.model = model
        self.year = year
        self.color = color 
        self.for_sale = for_sale

    def drive(self):
        print (f"You drive the {self.color} {self.model}.")
    
    def stop (self):
        print (f"You stop the {self.color} {self.model}.")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
def main():
    #creating some objects from the class car 
    car1 = Car("Mustang", 2024, "red", False)
    car2 = Car("Corvette", 2025, "yellow", True)
    car3 = Car("BMW", 2026, "blue", True)

    print (car1.model)
    print (car1.year)
    print (car1.color)
    print (car1.for_sale)

    car3.drive()
    car1.describe()
main()