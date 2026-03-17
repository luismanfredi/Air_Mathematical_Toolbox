from src.engine import add, sub, mul, div, power, sqrt, apply_binary, apply_unary
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (1, -1, 0),
    (-1, -1, -2),
    (-1, 0, -1),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 0),
    (1, -1, 2),
    (-1,-1, 0),
    (0, -1, 1),
    (0, 0, 0),
])
def test_sub(x, y, expected):
    assert sub(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 0, 0),
    (2, -1, -2),
])
def test_mul(x, y, expected):
    assert mul(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 1, 2),
    (0, 3, 0),
    (-2, 1, -2),
])
def test_div(x, y, expected):
    assert div(x, y) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

@pytest.mark.parametrize("x, y, expected", [
    (2, -1, 0.5),
    (-2, 2, 4),
    (4, 0.5, 2),
])
def test_power(x, y, expected):
    assert power(x, y) == expected

@pytest.mark.parametrize("x, expected", [
    (16, 4),
    (4, 2),
])
def test_sqrt(x, expected):
    assert sqrt(x) == expected

def test_sqrt_with_negative_num():
    with pytest.raises(ValueError):
        sqrt(-4)

def test_apply_binary_add():
    assert apply_binary("+", 1, 2) == 3

def test_apply_binary_sub():
    assert apply_binary("-", 1, 2) == -1

def test_apply_binary_mul():
    assert apply_binary("*", 1, 2) == 2

def test_apply_binary_div():
    assert apply_binary("/", 1, 2) == 0.5

def test_apply_binary_power():
    assert apply_binary("^", 1, 2) == 1

def test_apply_binary_error():
    assert apply_binary("?", 1, 3) == ValueError

def test_apply_unary_sqrt():
    assert apply_unary("sqrt", 4) == 2

def test_apply_unary_error():
    assert apply_unary("?", 1) == ValueError
