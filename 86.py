# Simple Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
person1 = Person("Alice", 30)

# Print attributes
print("Name:", person1.name)
print("Age:", person1.age)