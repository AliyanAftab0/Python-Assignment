import random

SIDES = 6

def roll_dice():
    dice1: int = random.randint(1, SIDES)
    dice2: int = random.randint(1, SIDES)
    total: int = dice1 + dice2
    print("Total of two dice:", total)

def main():
    dice1: int = 10
    print("dice1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("dice1 in main() is: " + str(dice1))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == "__main__":
    main()
