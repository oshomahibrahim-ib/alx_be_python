# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract',
                         'multiply', or 'divide').

    Returns:
        float or str: The numeric result (as a float) for successful operations,
                      or an error string for division-by-zero or invalid operation.
    """
    # Normalize operation input: remove surrounding whitespace and make lowercase
    op = operation.strip().lower()

    # Addition
    if op == 'add':
        return float(num1 + num2)

    # Subtraction
    elif op == 'subtract':
        return float(num1 - num2)

    # Multiplication
    elif op == 'multiply':
        return float(num1 * num2)

    # Division with zero handling
    elif op == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return float(num1 / num2)

    # Invalid operation
    else:
        return f"Error: Invalid operation '{operation}'. Must be 'add', 'subtract', 'multiply', or 'divide'."
