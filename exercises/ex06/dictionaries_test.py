"""Unit tests for dictionary functions."""
from exercises.ex06.dictionaries import invert, favorite_color

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert_kris():
    a: dict = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_freq():
    a: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"   