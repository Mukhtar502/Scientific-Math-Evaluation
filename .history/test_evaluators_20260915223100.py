import pytest
from math_evaluator import verify_mathematical_equivalence

def test_equivalent_expressions():
    assert verify_mathematical_equivalence("2*x + 3*x", "5*x") == True
    assert verify_mathematical_equivalence("sin(x)**2 + cos(x)**2", "1") == True

def test_non_equivalent_expressions():
    assert verify_mathematical_equivalence("x**2", "x**3") == False

def test_invalid_syntax():
    assert verify_mathematical_equivalence("2 * * x", "2*x") == False