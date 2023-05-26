import pytest
from exercice1 import Calculator

def test_addition():
    calculator = Calculator()
    result = calculator.add(37, 3)
    assert result == 40

def test_soustraction():
    calculator = Calculator()
    result = calculator.subtract(100, 1)
    assert result == 99

def test_multiplication():
    calculator = Calculator()
    result = calculator.multiply(25, 2)
    assert result == 50

def test_division():
    calculator = Calculator()
    result = calculator.divide(15, 3)
    assert result == 5.0

def test_puissance():
    calculator = Calculator()
    result = calculator.power(5, 2)
    assert result == 25

def test_racine():
    calculator = Calculator()
    result = calculator.sqrt(9)
    assert result == 3.0

def test_memory():
    calculator = Calculator()
    result = calculator.sqrt(16)
    assert result == 4.0
    memory = calculator.get_memory()
    assert memory == 4.0
    calculator.clear_memory()
    memory = calculator.get_memory()
    assert memory == 0

