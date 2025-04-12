import random
import time


def display_welcome():
    print(
        """
   ____                     _   _                 _____                      
  / ___|_   _  ___  ___ ___| \ | |_   _ _ __ ___|_   _| __ __ _  ___ ___ 
 | |  _| | | |/ _ \/ __/ __|  \| | | | | '__/ _ \ | || '__/ _` |/ __/ _ \\
 | |_| | |_| |  __/\__ \__ \ |\  | |_| | | |  __/ | || | | (_| | (_|  __/
  \____|\__,_|\___||___/___/_| \_|\__,_|_|  \___| |_||_|  \__,_|\___\___|
    """
    )
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    time.sleep(1)


def get_player_guess():
    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("That's not a valid number. Please try again.")


def give_hint(secret_number, guess):
    if abs(secret_number - guess) <= 5:
        return "Very hot!"
    elif abs(secret_number - guess) <= 15:
        return "Hot!"
    elif abs(secret_number - guess) <= 25:
        return "Warm."
    else:
        return "Cold."


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"\nYou have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        guess = get_player_guess()

        if guess == secret_number:
            print(
                f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!"
            )
            if attempts <= 5:
                print("⭐ Wow! You're really good at this!")
            return True

        hint = give_hint(secret_number, guess)
        if guess < secret_number:
            print(f"{hint} Too low! ", end="")
        else:
            print(f"{hint} Too high! ", end="")

        print(f"(Attempts left: {remaining_attempts})")

    print(f"\nGame over! The number was {secret_number}.")
    return False


def main():
    display_welcome()

    while True:
        play_game()

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
