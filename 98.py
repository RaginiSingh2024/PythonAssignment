 # Property Decorator
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price 

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

# Example Usage
product1 = Product("Laptop", 1200)
print(product1.price) 
product1.price = 1500 
print(product1.price) 
product1.price = -100  
print(product1.price)