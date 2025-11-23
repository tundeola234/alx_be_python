# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main program
def main():
    # Ask user for temperature
    temp_input = input("Enter the temperature to convert: ")

    # Validate temperature
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask user for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")

    elif unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# Run the program
if __name__ == "__main__":
    main()
