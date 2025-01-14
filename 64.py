# Polymorphism
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")
