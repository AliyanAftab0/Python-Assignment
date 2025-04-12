import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    numbers: list = []
    for i in range(N_NUMBERS):
        numbers.append(random.randint(MIN_VALUE, MAX_VALUE))
    for number in numbers:
        print(number, end=", ")

if __name__ == "__main__":
    main()