"""Repeating a beat in a loop."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
reps: int = int(input("How many times do you want to repeat it? "))
res: str = ""

i: int = 0

if reps <= 0:
    print("No beat...")
else:
    if reps == 1:
        print(beat)
    else:
        while i < reps:
            i = i + 1
            res = beat + " " + res

print(res)