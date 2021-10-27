"""Practice with dictionaries."""

__author__ = "123456789"


def main() -> None:
    a: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    print(favorite_color(a))


def invert(a: dict) -> dict:
    b: dict = dict()
    for key in a:
        new_key = a[key]
        if new_key in b:
            raise KeyError
        else:
            b[new_key] = key
    return b
        

def favorite_color(a: dict[str, str]) -> str:
    # save a default value for the most popular color
    mp: str = ""
    fm: dict[str, int] = dict()
    # "loop through the dict"
    # check current val against mp?
    # or, make a frequency map
    #     if val in mp, increment
    #     else, new val
    for key in a:
        val = a[key]
        print("value", val)
        if val in fm:
            print("found value as key! Incrementing")
            print(fm[val])
            fm[val] = fm[val] + 1
            print(fm[val])
        else:
            print("New value as key! Assigning")
            fm[val] = 1
            print(fm[val])
    print(fm)
    # pick the highest val of the frequency map
    max = 0
    for key in fm:
        if fm[key] >= max:
            mp = key
            max = fm[key]
    return mp

        

# Define your functions below

if __name__ == "__main__":
    main()
