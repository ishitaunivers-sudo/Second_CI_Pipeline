
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "34_check_sorted.py"

spec = importlib.util.spec_from_file_location("check_sorted", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_empty_list():
    assert module.is_sorted([]) is True


def test_equal_elements():
    assert module.is_sorted([2, 2, 2]) is True
