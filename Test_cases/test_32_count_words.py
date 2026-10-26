
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "32_count_words.py"

spec = importlib.util.spec_from_file_location("count_words", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_normal_sentence():
    assert module.count_words("Python is very easy") == 4


def test_extra_spaces():
    assert module.count_words("  Hello   World  ") == 2


def test_empty_sentence():
    assert module.count_words("") == 0


def test_one_word():
    assert module.count_words("Hello") == 1
