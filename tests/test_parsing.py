from src.parsing import _normalize, parse_command, parse_number, parse_op
import pytest

@pytest.mark.parametrize("s, expected", [
    ("1", "1"),
    (" 0     ", "0"),
    ("  Q", "q"),
    ("   qUIt  ", "quit"),
])
def test_normalize(s, expected):
    assert _normalize(s) == expected

@pytest.mark.parametrize("s, expected", [
    ("abc", None),
    ("q", ("COMMAND", "QUIT")),
    ("h", ("COMMAND", "HELP")),
    ("c", ("COMMAND", "CLEAR")),
    ("r", ("COMMAND", "HISTORY")),
])
def test_parse_command(s, expected):
    assert parse_command(s) == expected

@pytest.mark.parametrize("s, ans, expected", [
    (" 4", None, ("NUMBER", 4.0)),
    (" -101 ", None, ("NUMBER", -101.0)),
    ("ans", 3, ("NUMBER", 3.0)),
    ("ans", None, ("INVALID", "ANS_NOT_SET")),
    ("abc", None, ("INVALID", "NOT_A_NUMBER")),
    ("r", None, ("COMMAND", "HISTORY")),

])
def test_parse_number(s, ans, expected):
    assert parse_number(s, ans) == expected

@pytest.mark.parametrize("s, expected", [
    ("+", ("BINARY_OP", "+")),
    ("-", ("BINARY_OP", "-")),
    ("*", ("BINARY_OP", "*")),
    ("/", ("BINARY_OP", "/")),
    ("^", ("BINARY_OP", "^")),
    ("q", ("COMMAND", "QUIT")),
    ("h", ("COMMAND", "HELP")),
    ("sqrt", ("UNARY_OP", "sqrt")),
    ("abc", ("INVALID", "NOT_AN_OPERATOR")),
])
def test_parse_op(s, expected):
    assert parse_op(s) == expected