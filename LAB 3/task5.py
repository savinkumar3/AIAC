def read_temperature_input():
    """
    Reads a temperature value and its unit from the user.
    Returns:
        temp (float): The temperature value.
        unit (str): The unit of the temperature ('C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin).
    """
    print("Enter the temperature value followed by its unit (C for Celsius, F for Fahrenheit, K for Kelvin).")
    print("Example: 100 C")
    while True:
        user_input = input("Temperature and unit: ").strip().split()
        if len(user_input) != 2:
            print("Invalid input format. Please enter value and unit separated by a space (e.g., 100 C).")
            continue
        try:
            temp = float(user_input[0])
            unit = user_input[1].upper()
            if unit not in ['C', 'F', 'K']:
                print("Invalid unit. Please enter 'C', 'F', or 'K'.")
                continue
            return temp, unit
        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")

def convert_temperature(value, from_unit, to_unit):
    """
    Converts temperature from one unit to another.
    Args:
        value (float): The temperature value to convert.
        from_unit (str): The unit of the input temperature ('C', 'F', 'K').
        to_unit (str): The unit to convert to ('C', 'F', 'K').
    Returns:
        float: The converted temperature value.
    """
    # Convert input to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit")

    # Convert Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit")

def temperature_conversion_instructions():
    """
    Prints clear instructions for using the temperature conversion functions.
    """
    print("Temperature Conversion Tool Instructions:")
    print("1. When prompted, enter the temperature value followed by its unit (C, F, or K).")
    print("   For example: 37 C")
    print("2. Next, enter the unit you want to convert to (C, F, or K).")
    print("3. The program will display the converted temperature value.")
    print("Note: Valid units are:")
    print("   C - Celsius")
    print("   F - Fahrenheit")
    print("   K - Kelvin")

# Example usage:
if __name__ == "__main__":
    temperature_conversion_instructions()
    temp, from_unit = read_temperature_input()
    to_unit = input("Enter the unit to convert to (C, F, K): ").strip().upper()
    if to_unit not in ['C', 'F', 'K']:
        print("Invalid target unit.")
    else:
        converted = convert_temperature(temp, from_unit, to_unit)
        print(f"{temp} {from_unit} is {converted:.2f} {to_unit}")
