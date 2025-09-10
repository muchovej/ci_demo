import pytest

from src.add import add

def test_addition_happy_path():
    assert add(2,3) == 5

def test_neg_values():
    assert add(-2, -3) == -5

def test_add_floats():
    assert add(2.0, 3.0) == 5

def test_add_one_neg():
    assert add(2, -3) == -1

@pytest.mark.parametrize(
    "input1, input2, expected_value",
    [(2, 3, 5), (-2, -3, -5), (2.0, 3.0, 5.0), (2, -3, -1)],
)
def test_add(input1, input2, expected_value):
    assert add(input1, input2) == expected_value
