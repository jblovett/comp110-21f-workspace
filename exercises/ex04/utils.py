"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.

def all(input: list[int], given: int) -> bool:
    i = 0
    while i < len(input):
        if input[i] != given:
            return False
        i += 1
    return True


def is_equal(first: list[int], second: list[int]) -> bool:
    if len(first) != len(second):
        return False
    else:
        i = 0
        j = 0
        while i < len(first):
            if first[i] != second[j]:
                return False
            i += 1
            j += 1
    return True