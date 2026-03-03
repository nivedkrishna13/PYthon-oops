class Car:
    wheels = 4   # class attribute (shared)

    def __init__(self, brand, speed):
        self.brand = brand      # instance attribute
        self.speed = speed      # instance attribute

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} speed increased to {self.speed}")
car1 = Car("BMW", 100)

# attribute access (direct)
print(car1.brand)   # automatically accessed

# method call (manual)
car1.accelerate()