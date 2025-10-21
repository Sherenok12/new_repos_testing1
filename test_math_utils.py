from math_utils import factorial, average
import pytest

def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1

def test_factorial_zero():
    assert factorial(0) == 1

def test_average():
    assert average([2, 4, 6]) == 4

def test_average_error():
    import pytest
    with pytest.raises(ValueError):
        average([])

def test_factorial_error():
    with pytest.raises(ValueError):
        factorial(-3)
