"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730243388"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

selector: int = randint(1, 3)

fort_1: str = "Do what you want, not what you should."
fort_2: str = "There are NO accidents!"
fort_3: str = "it ain't easy being cheesy"

print("Your fortune cookie says...")
if selector == 1:
    print(fort_1)
else:
    if selector == 2:
        print(fort_2)
    else:
        if selector == 3:
            print(fort_3)
print(selector)
print("Now go spread positive vibes!")
