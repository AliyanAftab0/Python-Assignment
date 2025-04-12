import random
import time


def display_welcome():
    print(
        """
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/                       
    """
    )
    print("Welcome to Hangman!")
    print("Guess the word before the man gets hanged!\n")
    time.sleep(1)


def load_words():
    # Categories of words
    categories = {
        "animals": ["elephant", "giraffe", "kangaroo", "dolphin", "rhinoceros"],
        "fruits": ["watermelon", "strawberry", "pineapple", "blueberry", "raspberry"],
        "countries": ["australia", "brazil", "canada", "denmark", "ethiopia"],
    }

    print("Choose a category:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category.capitalize()}")

    while True:
        try:
            choice = int(input("Enter category number: ")) - 1
            if 0 <= choice < len(categories):
                category = list(categories.keys())[choice]
                return random.choice(categories[category])
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")


def display_hangman(tries):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """,
    ]
    return stages[tries]


def play_game():
    word = load_words()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    correct_letters = set()
    tries = 0
    max_tries = 6

    print("\nLet's begin! The word has", len(word), "letters.")

    while len(word_letters) > 0 and tries < max_tries:
        print("\n" + display_hangman(tries))

        # Show current progress
        word_list = [letter if letter in correct_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))
        print("Used letters:", " ".join(sorted(used_letters)))

        # Get user input
        while True:
            guess = input("Guess a letter: ").lower()
            if guess in alphabet - used_letters:
                used_letters.add(guess)
                break
            elif guess in used_letters:
                print("You've already used that letter. Try again.")
            else:
                print("Invalid input. Please enter a single letter.")

        # Check if guess is correct
        if guess in word_letters:
            word_letters.remove(guess)
            correct_letters.add(guess)
            print("Good guess!")
        else:
            tries += 1
            print(
                f"Oops! That letter is not in the word. Tries left: {max_tries - tries}"
            )

    # Game over - show result
    print("\n" + display_hangman(tries))
    if tries == max_tries:
        print(f"Sorry, you lost! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")


def main():
    display_welcome()

    while True:
        play_game()

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing Hangman! Goodbye!")
            break


if __name__ == "__main__":
    main()
