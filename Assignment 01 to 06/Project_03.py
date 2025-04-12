import random
import time


def display_welcome():
    print(
        """
   ____                     _   _                 _   _             
  / ___|_   _  ___  ___ ___| \ | |_   _ _ __ ___| | | |___  ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|  \| | | | | '__/ _ \ | | / __|/ _ \ '__|
 | |_| | |_| |  __/\__ \__ \ |\  | |_| | | |  __/ |_| \__ \  __/ |   
  \____|\__,_|\___||___/___/_| \_|\__,_|_|  \___|\___/|___/\___|_|   
    """
    )
    print("Welcome to Guess the Number (User Version)!")
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    time.sleep(1)
    input("Press Enter when you're ready to begin...")


def computer_guess():
    low = 1
    high = 100
    attempts = 0
    max_attempts = 7  # Computer can guess in max 7 attempts using binary search

    print("\nOkay, I'll start guessing now!")

    while attempts < max_attempts:
        attempts += 1
        guess = random.randint(low, high) if attempts == 1 else (low + high) // 2

        print(f"\nMy guess #{attempts}: Is it {guess}?")
        response = input(
            "(Enter 'c' if correct, 'h' if your number is higher, 'l' if lower): "
        ).lower()

        while response not in ["c", "h", "l"]:
            print("Invalid input! Please enter 'c', 'h', or 'l'.")
            response = input(
                "(Enter 'c' if correct, 'h' if higher, 'l' if lower): "
            ).lower()

        if response == "c":
            print(f"\n🎉 Hooray! I guessed your number in {attempts} attempts!")
            if attempts <= 3:
                print("🤖 I'm getting good at this!")
            return True
        elif response == "h":
            low = guess + 1
            print(f"Okay, your number is higher than {guess}...")
        else:
            high = guess - 1
            print(f"Okay, your number is lower than {guess}...")

        if low > high:
            print("\nWait a minute... you must have changed your number!")
            return False

    print(
        f"\nI couldn't guess your number in {max_attempts} attempts. Did you follow the rules?"
    )
    return False


def main():
    display_welcome()

    while True:
        print("\nThink of a number between 1 and 100. I'll try to guess it!")
        print("Remember the number in your head and I'll ask you questions to find it.")

        computer_guess()

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
