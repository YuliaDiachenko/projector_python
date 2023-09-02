class Product:  
    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality

class Book(Product):
    def __init__(self, author, name, price, quality):
        super().__init__(name, price, quality)
        self.author = author
    def read(self):
        print(f'This book is {self.name} written by {self.author} , {self.quality}. It costs {self.price} USD.')

book1 = Book("Jack London", "Martin Eden", 299, "new")
book1.read()