import random

NUM_ROUNDS = 5


def play_round(round_num, score):
    print(f"\nRound {round_num}")
    your_num = random.randint(1, 100)
    comp_num = random.randint(1, 100)

    print(f"Your number is {your_num}")

    while True:
        guess = input(
            "Do you think your number is higher or lower than the computer's?: "
        ).lower()
        if guess in ["higher", "lower"]:
            break
        print("Please enter either higher or lower:")

    correct = False
    if guess == "higher" and your_num > comp_num:
        correct = True
    elif guess == "lower" and your_num < comp_num:
        correct = True

    print(f"The computer's number was {comp_num}")

    if correct:
        score += 1
        print("You were right!", end=" ")
    else:
        print("Aww, that's incorrect.", end=" ")

    print(f"Your score is now {score}")
    return score


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)

    print("\nThanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
