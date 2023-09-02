#3. Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate and brake. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5.

class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    
    def __str__(self):
        return f'This car is {self.brand} {self.model} {self.year} year with speed {self.speed} km/h'

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

BMW = Car("BMW", "X1", 2019, 100)
print(BMW)

BMW.accelerate()
BMW.accelerate()
BMW.brake()
print(BMW)