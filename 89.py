# Class with Default Values
 class Car:
    def __init__(self, make="Toyota", model="Camry", year=2023):
        self.make = make
        self.model = model
        self.year = year

# Create instances 
car1 = Car()  # Using default values
car2 = Car("Honda", "Civic", 2022) 

print(car1.make, car1.model, car1.year)
print(car2.make, car2.model, car2.year)