'''
Nested Class = A class defined within another class 
               class Outer
                    class Inner
Benefits: 
    - Allows you to logically group classes that are closely related 
    - Encapsulate private details that aren't relevent outside of the outer class 
    - Keeps the namespace clean; reduces the posibility of naming conflicts
'''
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} works as {self.position}"

    # these methods belongs to the Company class 
    def __init__(self, company_name):
        self.company_name = company_name
        self.empolyees = []     #list of objects
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.empolyees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.empolyees]
    
def main():
    company1 = Company("Muslim-Vision")
    company1.add_employee("Mohammed","CEO")
    company1.add_employee("Atef","waiter")
    for employee in company1.list_employees():
        print(employee)

main()

