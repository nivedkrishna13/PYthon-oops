class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # inherited
d.bark()

## singlelevel 
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

## multilevel
class Animal:
    def breathe(self):
        print("Breathing")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

d = Dog()
d.breathe()
d.walk()
d.bark()

## heirarchiel
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# hydrid
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass