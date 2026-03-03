class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")   
emp1 = employee("Nemo", 30, 50000)
print(emp1.name)   # public attribute
print(emp1.age)    # public attribute
print(emp1.__salary)