"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

addition: str = TREE

depth: int = int(input("Depth: "))

i: int = 0

while i < depth:
    print(TREE)
    TREE = TREE + addition
    i += 1

print("\n")

while 