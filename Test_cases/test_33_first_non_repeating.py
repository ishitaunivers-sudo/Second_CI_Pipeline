
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "33_first_non_repeating.py"

spec = importlib.util.spec_from_file_location("first_non_repeating", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_first_non_repeating():
    assert module.first_non_repeating("swiss") == "w"


def test_all_repeated():
    assert module.first_non_repeating("aabb") is None


def test_single_character():
    assert module.first_non_repeating("x") == "x"


def test_empty_string():
    assert module.first_non_repeating("") is None
