# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Return the area of the shape. Subclasses must override this."""
        raise NotImplementedError("Subclasses must implement the area() method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
