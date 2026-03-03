class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


class Cow:
    def speak(self):
        return "Moo"


# Create objects
animals = [Dog(), Cat(), Cow()]

# Polymorphic loop
for animal in animals:
    print(animal.speak())