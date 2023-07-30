# Build a typing tester.
# This should show the user some text, and then challenge them to type it
# while timing them and scoring them on for accuracy.

# 1-The user should specify if he wants to play or quit def pORq
# 2- if yes, the game will show him a text and start a timer def rantext def timer
# 3- if the input matches the text in 20s the player wins def main
import time
from inputimeout import inputimeout


def pORq(firstinput):
    if firstinput.lower() == "p":
        print("Lets start the game! ")
        return True
    elif firstinput.lower() == "q":
        print("The game will stop now! ")
        return False
    else:
        print("The input must be either p or q! start the game again")
        return False


def rantext():
    import random

    with open('randomsentences.txt') as f:
        lines = f.readlines()
        TheSentence = random.choice(lines)
        print(f"Write this sentence in 10 seconds... \n {TheSentence}")
    return TheSentence


def timer():



    # Try block of code
    # and handle errors
    try:

        # Take timed input using inputimeout() function
        time_over = inputimeout(prompt='Starting time...Enter the text:', timeout=10)

    # Catch the timeout error
    except Exception:

        # Declare the timeout statement
        time_over = 'Your time is over!'
        return time_over


    # Print the statement on timeoutprint(time_over)


def comparison(text, TheSentence):
    if text == TheSentence:
        print("You have won")
    else:
        print("You lost! Better luck next time...")


def main():
    firstinput = input("Enter p to play or q to stop: ")
    while pORq(firstinput):
        comparison(rantext(), timer())
        firstinput = input("Enter p to play or q to stop: ")


main()
