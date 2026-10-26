import importlib.util
from pathlib import Path

file_path = (
    Path(__file__).parent.parent
    / "Code"
    / "31_pangram.py"
)

spec = importlib.util.spec_from_file_location(
    "pangram_module", file_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False 
