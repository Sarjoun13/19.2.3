import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_append_calculate_correctly(self):
        assert self.calc.adding(self, 2, 3) == 5

    def test_append_subtraction_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2