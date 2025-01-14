 # Constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance
car1 = Car("Toyota", "Camry", 2023)

# Display details
print("Make:", car1.make)
print("Model:", car1.model)
print("Year:", car1.year)