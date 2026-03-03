class student:
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    def change_school(self,school):
        self.school = school
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school}")

s1 = student("Nemo", 20, "ABC University")
s1.display()   # Name: Nemo, Age: 20, School: ABC University
s1.change_school("XYZ University")
s1.display()   # Name: Nemo, Age: 20, School: XYZ University
