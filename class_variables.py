#class variables = shared among all instances of a class
#                  Defined outside the constructor method(initalization)
#                  Allow u to share data among all objects created from that class 


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self,name, age):
        self.name = name
        self.age = age 
        Student.num_students += 1

def main():
    student1 = Student("Spongebob", 30)
    student2 = Student("Patrick", 36)
    student3 = Student("Mohammed", 22)

    ''' it's recommended to access the class variables using 
    the class name itself'''

    print (f"My graduating class of  {Student.class_year} has {Student.num_students} students.") 
    print (student1.name)
    print (student2.name)
    print (student3.name)
main()









