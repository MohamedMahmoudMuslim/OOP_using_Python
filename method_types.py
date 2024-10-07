'''
# Instance Methods: Best for operations on instances of the class (objects) 
# 
# Class Methods: Allows operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself
#                Best for class-level data or require access to the class itself
#
# Static Methods: A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions that do not need access to class data
#
# Magic Methods: Dunder methods (double underscore) __init__, __str__, __eq__,__gt__,__lt__
#                They are automatically called by many of Python's built-in operations.
#                They allow devolopers to define or customize the behavior of objects
'''

class Employee:
    valid_positions = ["Manager", "Cashier", "Cook"]

    def __init__(self, name, position):
        self.name = name
        if position in Employee.valid_positions: 
            self.position = position
        

    def get_details(self): 
        return f"{self.name} works as {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        return position in Employee.valid_positions
    
def static_method():
    employee1 = Employee("Mohammed", "Manager")
    print(Employee.is_valid_position("Cashier"))
#function(method) call 
static_method()

class Student:
    num_students = 0 
    total_gpa = 0 

    # Magic Method 
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        Student.num_students += 1
        Student.total_gpa += gpa 

    # Instance Method 
    def get_num_students(self):
        return f"Student name: {self.name}, GPA: {self.gpa}"
    

    @classmethod
    def get_num_students(cls):
        return cls.num_students
    
    @classmethod
    def get_avg_gpa(cls):
        if Student.num_students == 0 :
            return f"Students # cannot be zero!"
        else:
            return  cls.total_gpa / cls.num_students
        
def class_method():
    student1 = Student("Mohammed", 3.4)
    student2 = Student("Ashraf", 4.0)
    student3 = Student("Samir", 2.6)
    print(f"Number of students = {Student.get_num_students()}")
    print(f"Average GPA = {Student.get_avg_gpa():.2f}")
class_method()


class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, keyword):
        if keyword == "title":
            return self.title
        elif keyword == "author":
            return self.author
        elif keyword == "pages":
            return self.num_pages
        else:
            return f"Key {keyword} was not found."
        
        
def magic_method():
    book1 = Book("Harry Potter", "J.K. Rowling", 490)
    book2 = Book("The Hobbit", "J.R.R. Tolkein", 450)
    print(book1)    # will print the address of the object 
    # to print the content of object we use magic mehtod calld __str__

    print(book1 == book2)
    print(book1 > book2)
    print(book1 < book2)
    print (book1 + book2)
    print('Potter')
    print(book1["author"])
    print(book2["title"])
    print(book2["pages"])
magic_method()

