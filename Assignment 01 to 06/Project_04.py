import random
import time


def display_welcome():
    print(
        """
    ____            _       ___                 ____                      
   |  _ \ ___   ___| | __  / _ \ _ __   ___   / ___| _ __   ___  ___ ___ 
   | |_) / _ \ / __| |/ / | | | | '_ \ / _ \  \___ \| '_ \ / _ \/ __/ __|
   |  _ < (_) | (__|   <  | |_| | |_) | (_) |  ___) | |_) |  __/\__ \__ \\
   |_| \_\___/ \___|_|\_\  \___/| .__/ \___/  |____/| .__/ \___||___/___/
                                |_|                 |_|                  
    """
    )
    print("Welcome to Rock, Paper, Scissors!")
    print("First to win 3 rounds wins the game!\n")
    time.sleep(1)


def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ["rock", "paper", "scissors", "r", "p", "s"]:
            if choice == "r":
                return "rock"
            elif choice == "p":
                return "paper"
            elif choice == "s":
                return "scissors"
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"


def display_result(player_choice, computer_choice, winner):
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def play_game():
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        print(f"\nCurrent Score - You: {player_score} | Computer: {computer_score}")
        print("-------------------------------")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, winner)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

    print("\n=================================")
    if player_score == 3:
        print("🎉 Congratulations! You won the game!")
    else:
        print("💻 Computer wins the game! Better luck next time!")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    print("=================================")


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
