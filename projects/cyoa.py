from random import randint

RAT: str = "\U0001F400"


def main() -> None:
    global points
    points = 0
    global playing
    playing = True
    greet()
    # set globals before loop
    while playing:
        print(f"Happiness Points: {points}")
        branch: str = input("Take your rat on a walk or stay inside? Type 'inside' or 'outside'.")
        if branch == "inside":
            inside()
        elif branch == "outside":
            points = outside(points) 
        elif branch == "quit":
            playing = False
        else:
            print("make sense fool!")
    print(f"{RAT} Total Happiness Points: {points}. Thanks for playing! {RAT}")


def greet() -> None:
    print("Greetings! Take care of your rat.")
    global player
    player = input("What is your rat's name? ")


def inside() -> None:
    global points
    global playing
    branch: str = input("Play with your rat, let them sleep, or feed them? Type 'play', 'sleep', or 'feed'. Type 'quit' to quit.")
    if branch == "play":
        points += 20
        print(f"Your rat is very entertained. Happiness Points: {points}")
    elif branch == "sleep":
        points += 5
        print(f"Your rat is well rested but kinda bored. Happiness Points: {points}")
    elif branch == "feed":
        points += 10
        print(f"There is a party in your rat's tummy. Happiness points: {points}")
    elif branch == "quit":
        playing = False
    else:
        print("make sense fool")


def outside(points: int) -> int:
    leash: str = input("Did you bring a rat leash? Type 'yes' or 'no'.")
    global player
    global playing
    if leash == "yes":
        exploring = True
        while exploring:
            branch: str = input("Where will you take your rat? \n Type 'park', 'mall', or 'car' to decide where to go. \n Type 'home' to go home. Type 'quit' to stop playing.")
            if branch == "park":
                points += 20
                random_choice = randint(0, 3)
                if random_choice == 0:
                    print(f"{player} wanders through the trees and makes a new squirell friend.")
                elif random_choice == 1:
                    print(f"{player} climbs a tree and eats an acorn like  a squirell.")
                elif random_choice == 2:
                    print(f"{player} soaks up some sun and gets a tan.")
                elif random_choice == 3:
                    print(f"{player} squeaks really loudly but can't sing very well.")

            elif branch == "mall":
                print(f"{player} eats an entire pretzel and dodges many footsteps.")
                points += 10
            elif branch == "car":
                print(f"{player} sticks their nose out the window and feels so alive!")
            elif branch == "home":
                exploring = False
            elif branch == "quit":
                playing = False
                exploring = False
    elif leash == "no":
        print("Your rat is lost forever")
        playing = False
    
    return points


if __name__ == "__main__":
    main()