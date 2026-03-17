from src.formatting import fmt
import pytest

@pytest.mark.parametrize("n, expected", [
    (5.0, "5"),
    (-4.0, "-4"),
    (2.65, "2.65"),
    (4.01938475839, "4.0193847584"),
    (0.00000000005, "0.0000000001"),
    (0.00000000001, "0"),
])
def test_fmt(n, expected):
    assert fmt(n) == expected