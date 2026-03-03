# Create a class Laptop with:

# attributes: brand, price

# method: display_info()

# Create 2 objects and print their info.


class laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Brand = {self.brand} \nPrice = {self.price}")

nived = laptop("Hp",67000)

nived.display_info()