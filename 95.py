# Magic Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: Name={self.name}, Age={self.age}"

# Example Usage
person1 = Person("Alice", 30)
print(person1)  # Calls the __str__ method