# Method in Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Create an instance
person1 = Person("Bob", 25)

# Call the greet method
person1.greet()