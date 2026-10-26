
def missing_number(numbers):
    result = len(numbers)

    for i, number in enumerate(numbers):
        result ^= i ^ number

    return result
