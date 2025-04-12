import time
import sys
import winsound  # For Windows sound alerts
import platform
from datetime import datetime, timedelta


def display_welcome():
    print(
        """
     ____                  _                 _   _             
    / ___|___  _ __   ___ | |_ _ __ ___   __| | (_)_ __   __ _ 
   | |   / _ \| '_ \ / _ \| __| '_ ` _ \ / _` | | | '_ \ / _` |
   | |__| (_) | | | | (_) | |_| | | | | | (_| | | | | | | (_| |
    \____\___/|_| |_|\___/ \__|_| |_| |_|\__,_| |_|_| |_|\__, |
                                                          |___/ 
    """
    )
    print("Welcome to Python Countdown Timer!")
    print("Set a timer for any duration (hours:minutes:seconds)\n")


def play_sound():
    """Play alert sound appropriate for the OS"""
    if platform.system() == "Windows":
        winsound.Beep(1000, 1000)  # Frequency, Duration in ms
    else:
        # Mac/Linux - print ASCII bell character
        sys.stdout.write("\a")
        sys.stdout.flush()


def get_time_input():
    """Get valid time input from user in HH:MM:SS format"""
    while True:
        time_str = input("Enter countdown time (HH:MM:SS or MM:SS or SS): ")
        try:
            # Parse the time string into hours, minutes, seconds
            parts = list(map(int, time_str.split(":")))

            if len(parts) == 3:  # HH:MM:SS
                hours, minutes, seconds = parts
            elif len(parts) == 2:  # MM:SS
                hours = 0
                minutes, seconds = parts
            elif len(parts) == 1:  # SS
                hours, minutes = 0, 0
                seconds = parts[0]
            else:
                raise ValueError("Invalid time format")

            # Validate each component
            if seconds >= 60 or minutes >= 60:
                raise ValueError("Seconds or minutes cannot be ≥60")
            if any(t < 0 for t in (hours, minutes, seconds)):
                raise ValueError("Time values cannot be negative")

            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds <= 0:
                raise ValueError("Timer duration must be greater than 0")

            return hours, minutes, seconds

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def format_time(seconds):
    """Convert seconds to HH:MM:SS format"""
    return str(timedelta(seconds=seconds))


def run_timer(hours, minutes, seconds):
    """Run the countdown timer with visual progress"""
    total_seconds = hours * 3600 + minutes * 60 + seconds
    end_time = datetime.now() + timedelta(seconds=total_seconds)

    print("\nTimer started! Press Ctrl+C to stop early.")
    print(f"Counting down from {format_time(total_seconds)}...")

    try:
        while total_seconds > 0:
            # Calculate remaining time
            remaining = end_time - datetime.now()
            total_seconds = max(0, int(remaining.total_seconds()))

            # Display progress
            sys.stdout.write("\r" + format_time(total_seconds) + " remaining ")
            sys.stdout.flush()

            # Check every 0.1 seconds for smoother display
            time.sleep(0.1)

        # Timer complete
        print("\n\nTIME'S UP!")
        play_sound()

    except KeyboardInterrupt:
        print("\n\nTimer stopped early!")
        return


def main():
    display_welcome()

    while True:
        print("\nMenu:")
        print("1. Start new timer")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            hours, minutes, seconds = get_time_input()
            run_timer(hours, minutes, seconds)
        elif choice == "2":
            print("\nThanks for using the Countdown Timer! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
