class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return len(self.title)
    def __add__(self,other):
        return f"{self.title} and {other.title}"
b1 = book("Python OOPS","Nived")
b2 = book("Data Science","Nived")
print(b1)   # calls __str__ automatically
print(len(b1))  # calls __len__ automatically
print(b1 + b2)  # calls __add__ automatically