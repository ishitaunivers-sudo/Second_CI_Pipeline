
import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "code" / "39_transpose_matrix.py"

spec = importlib.util.spec_from_file_location("transpose_matrix", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_square_matrix():
    assert module.transpose_matrix([[1, 2], [3, 4]]) == [
        [1, 3],
        [2, 4]
    ]


def test_rectangular_matrix():
    assert module.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_empty_matrix():
    assert module.transpose_matrix([]) == []


def test_single_row():
    assert module.transpose_matrix([[1, 2, 3]]) == [
        [1],
        [2],
        [3]
    ]
