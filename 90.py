#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Create instances
animal1 = Animal("Generic Animal")
dog1 = Dog("Buddy")

animal1.speak() 
dog1.speak()