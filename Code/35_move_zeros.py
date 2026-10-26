
def move_zeros(numbers):
    non_zeros = [n for n in numbers if n != 0]
    zeros = [n for n in numbers if n == 0]
    return non_zeros + zeros
