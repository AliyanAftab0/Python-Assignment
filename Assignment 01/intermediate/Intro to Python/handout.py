def calculate_mars_weight():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * 0.378
    print(f"The equivalent on Mars: {round(mars_weight, 2)}")


def calculate_planetary_weight():
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14,
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in gravity_constants:
        planetary_weight = earth_weight * gravity_constants[planet]
        print(f"The equivalent weight on {planet}: {round(planetary_weight, 2)}")
    else:
        print("Invalid planet entered.")

calculate_planetary_weight()
