import pytest
from math_utils import factorial, average, is_even, max_difference, normalize


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-3)


def test_average():
    assert average([2, 4, 6]) == 4
    with pytest.raises(ValueError):
        average([])


def test_is_even():
    assert is_even(2) is True
    assert is_even(5) is False


def test_max_difference():
    assert max_difference([1, 5, 10]) == 9
    assert max_difference([-3, -1, -7]) == 6
    with pytest.raises(ValueError):
        max_difference([])


def test_normalize():
    result = normalize([2, 4, 6])
    assert result == [0.0, 0.5, 1.0]

    # коли всі числа однакові — повертає список з 0.5
    result_same = normalize([5, 5, 5])
    assert result_same == [0.5, 0.5, 0.5]

    with pytest.raises(ValueError):
        normalize([])
