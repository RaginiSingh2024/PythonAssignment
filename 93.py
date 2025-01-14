#Polymorphism
from math import pi

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing a Circle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

# Example Usage
shapes = [Circle(5), Triangle()]
for shape in shapes:
    shape.draw()