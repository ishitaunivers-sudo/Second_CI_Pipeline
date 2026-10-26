
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "40_gcd.py"

spec = importlib.util.spec_from_file_location("gcd_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_gcd_normal():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime():
    assert module.gcd(7, 13) == 1


def test_gcd_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_negative():
    assert module.gcd(-12, 18) == 6


def test_gcd_both_zero():
    assert module.gcd(0, 0) == 0
