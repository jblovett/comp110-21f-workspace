"""List utility functions part 2."""

__author__ = "123456789"

# Define your functions below


def only_evens(input: list) -> list:
    i = 0
    output = list()
    while i < len(input):
        val = input[i]
        if val % 2 == 0:
            output.append(val)
        i += 1
    return output


def sub(start: int, end: int, input: list) -> list:
    output = list()
    length = len(input)
    if start < 0:
        start = 0
    if end > length:
        end = length
    if length == 0 or start > length or end <= 0:
        return output
    while start < end:
        output.append(input[start])
        start += 1
    return output