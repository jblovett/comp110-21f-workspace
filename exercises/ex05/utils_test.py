"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub

__author__ = "123456789"


def test_all_evens():
    all_evens: list = [2, 4, 6]
    assert only_evens(all_evens) == [2, 4, 6]


def test_sub():
    short: list = [2, 5, 4, 3]
    assert sub(1, 4, short) == [5, 4, 3]