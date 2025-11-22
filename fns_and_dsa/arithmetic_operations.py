# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.
                         Input is case-insensitive and may include surrounding whitespace.

    Returns:
        float or str:
            - The numeric result for successful operations (always a float when numeric).
            - A specific error string "Error: Cannot divide by zero" when attempting to divide by zero.
            - A specific error string "Error: Invalid operation '<operation>'." for unsupported operations.
    """
    # 1) Normalize the operation input (trim whitespace, make lowercase)
    op = operation.strip().lower()

    # 2) Handle the four supported operations
    if op == 'add':
        return float(num1 + num2)           # ensure float type

    elif op == 'subtract':
        return float(num1 - num2)

    elif op == 'multiply':
        return float(num1 * num2)

    elif op == 'divide':
        # 3) Division: check for zero to avoid ZeroDivisionError
        if num2 == 0:
            # Return a specific string the main.py (or any checker) can recognise
            return "Error: Cannot divide by zero"
        return float(num1 / num2)

    # 4) If operation not recognized, return a clear error string
    else:
        return f"Error: Invalid operation '{operation}'. Must be 'add', 'subtract', 'multiply', or 'divide'."
