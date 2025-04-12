def main():
    user_input_in_fahrenheit: str = input("Enter temperature in Fahrenheit: ")
    # Convert the input string to a float
    fahrenheit: float = float(user_input_in_fahrenheit)
    # Convert Fahrenheit to Celsius using the formula
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    # Print the result
    print(f"Temperature: {fahrenheit}°F = {degrees_celsius:.2f}°C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()