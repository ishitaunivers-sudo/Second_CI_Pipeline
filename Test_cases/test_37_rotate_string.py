
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "37_rotate_string.py"

spec = importlib.util.spec_from_file_location("rotate_string", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_rotate_two_positions():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_full_length():
    assert module.rotate_string("abc", 3) == "abc"


def test_rotate_empty_string():
    assert module.rotate_string("", 2) == ""


def test_rotate_more_than_length():
    assert module.rotate_string("abcd", 6) == "cdab"


def test_rotate_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"
