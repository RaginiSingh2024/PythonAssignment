# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Example Usage
point1 = Point(2, 3)
point2 = Point(5, 1)
point3 = point1 + point2
print(f"Result: x={point3.x}, y={point3.y}")