# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.

    Parameters:
        numerator -- value convertible to float (often a string from sys.argv)
        denominator -- value convertible to float

    Returns:
        A string with the result, or an error message:
          - "The result of the division is X" on success
          - "Error: Cannot divide by zero." if denominator is zero
          - "Error: Please enter numeric values only." if inputs cannot be converted to float
    """
    # Attempt to convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."

    # Attempt division and catch division-by-zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Successful division
    return f"The result of the division is {result}"
