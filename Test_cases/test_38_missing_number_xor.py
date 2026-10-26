
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "38_missing_number_xor.py"

spec = importlib.util.spec_from_file_location("missing_number_xor", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_missing_middle():
    assert module.missing_number([3, 0, 1]) == 2


def test_missing_last():
    assert module.missing_number([0, 1, 2, 3]) == 4


def test_missing_zero():
    assert module.missing_number([1, 2, 3]) == 0


def test_empty_list():
    assert module.missing_number([]) == 0
