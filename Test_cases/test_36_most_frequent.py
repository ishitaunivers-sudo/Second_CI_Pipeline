
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "36_most_frequent.py"

spec = importlib.util.spec_from_file_location("most_frequent", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_most_frequent():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_single_element():
    assert module.most_frequent([5]) == 5


def test_empty_list():
    assert module.most_frequent([]) is None


def test_repeated_string():
    assert module.most_frequent(["a", "b", "a"]) == "a"
