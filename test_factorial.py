import pytest
from factorial import calculate_factorial

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_one():
    assert calculate_factorial(1) == 1

def test_factorial_positive_numbers():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(7) == 5040

def test_factorial_negative_number():
    with pytest.raises(ValueError):
        calculate_factorial(-3)

def test_factorial_invalid_type():
    with pytest.raises(TypeError):
        calculate_factorial(3.5)
