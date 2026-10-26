
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "35_move_zeros.py"

spec = importlib.util.spec_from_file_location("move_zeros", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_zeros_at_end():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert module.move_zeros([0, 0]) == [0, 0]


def test_empty_list():
    assert module.move_zeros([]) == []
