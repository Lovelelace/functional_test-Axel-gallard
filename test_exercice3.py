import pytest
from math import pi
from exercice3 import Shape, Rectangle, Circle, Square

def test_rectangle():
    rectangle = Rectangle(4, 5)
    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18

    rectangle = Rectangle(7, 3)
    assert rectangle.area() == 21
    assert rectangle.perimeter() == 20

def test_cercle():
    circle = Circle(3)
    assert circle.area() == pi * 3 ** 2
    assert circle.perimeter() == 2 * pi * 3

    circle = Circle(5)
    assert circle.area() == pi * 5 ** 2
    assert circle.perimeter() == 2 * pi * 5

def test_carré():
    square = Square(4)
    assert square.area() == 16
    assert square.perimeter() == 16

    square = Square(6)
    assert square.area() == 36
    assert square.perimeter() == 24
