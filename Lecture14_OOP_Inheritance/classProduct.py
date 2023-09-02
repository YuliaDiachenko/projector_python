class Product:  
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, author, name, price, quantity):
        super().__init__(name, price, quantity)
        self.author = author
    def read(self):
        print(f'This book is {self.name} written by {self.author} , {self.quantity} . It costs {self.price} USD.')

book1 = Book("Jack London", "Martin Eden", 299, "new")
book1.read()