# Class definition
class Student:
    # constructor
    def __init__(self, name, marks):
        self.name = name      # attribute
        self.marks = marks    # attribute

    # method
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# Object creation
s1 = Student("Nemo", 95)
s1.display()