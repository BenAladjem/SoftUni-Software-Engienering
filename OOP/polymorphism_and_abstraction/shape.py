import math


class Shape:
    def get_area(self):
        return None

class Triangle(Shape):
    def __init__(self, a, h_a):
        self.h_a = h_a
        self.a = a

    def get_area(self):
        s = self.a * self.h_a * 0.5
        return s

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def get_area(self):
        s = self.a ** 2
        return s


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        s = self.r * self.r * 3.14
        return s
shapes = [Triangle(3, 6), Triangle(5, 8), Square(4), Circle(10), Triangle(2, 3)]

for shape in shapes:

    print(shape.get_area())