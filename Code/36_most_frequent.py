
from collections import Counter


def most_frequent(numbers):
    if not numbers:
        return None
    return Counter(numbers).most_common(1)[0][0]
