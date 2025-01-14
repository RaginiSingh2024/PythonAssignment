# Multiple Classes (Inheritance)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 

# Example Usage
square1 = Square(5)
print("Area of Square:", square1.area())