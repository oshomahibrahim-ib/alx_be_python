# temp_conversion_tool.py

# Global conversion factors (module-level globals)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Expects fahrenheit to be a numeric value (float or int).
    """
    # Use the global factor (read-only access; no 'global' declaration needed)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Expects celsius to be a numeric value (float or int).
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def parse_temperature_input(value_str):
    """
    Parse the user-provided temperature string into a float.
    If parsing fails, raise ValueError with the required message.
    """
    try:
        return float(value_str)
    except (TypeError, ValueError):
        # Requirement: raise an error with this exact message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    # Prompt the user for the temperature value
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric input and raise the specific error if invalid
    try:
        temp_value = parse_temperature_input(temp_input)
    except ValueError as err:
        # Print the message and exit cleanly (or re-raise if you prefer crash behavior)
        print(err)
        return

    # Prompt for unit and normalize
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ("C", "F"):
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    # Perform conversion and display results
    if unit == "F":
        celsius = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius}°C")
    else:  # unit == "C"
        fahrenheit = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F")

if __name__ == "__main__":
    main()
