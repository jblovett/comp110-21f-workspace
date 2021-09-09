"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")

index: int = 0
counter: int = 0

while index < len(word):
    if word[index] == letter:
        counter = counter + 1
    index = index + 1
    
print("Count: " + str(counter))
