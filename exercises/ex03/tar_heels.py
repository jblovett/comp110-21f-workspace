"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...

word: str = input("Enter a word: ")
length: int = len(word)
dup: bool = False

comparison: int = 0
current: int = 0

while current < length:
    comparison = current + 1
    # problem, can't compare the same letters, or else always true!
    # solution: start the comparison on the character after the current
    # core concept: we need a current character, and we need following characters to compare
    while comparison < length:
        if word[current] == word[comparison]:
            dup = True
        comparison += 1
    current += 1

print("Found duplicate: " + str(dup))