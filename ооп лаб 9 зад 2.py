import math
class RightTriangle:
    def __init__(self, leg1, leg2):
        self.leg1 = leg1
        self.leg2 = leg2
    def area(self):
        return (self.leg1 * self.leg2) / 2
class ArbitraryTriangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
right_triangle=RightTriangle(3, 4)
arbitrary_triangle=ArbitraryTriangle(5, 6, 7)
print("Площадь прямоугольного треугольника:", right_triangle.area())
print("Площадь произвольного треугольника:", arbitrary_triangle.area())
