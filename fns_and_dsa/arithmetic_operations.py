# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
      num1 -- first number
      num2 -- second number
      operation -- one of: 'add', 'subtract', 'multiply', 'divide'

    Returns:
      float result for valid operations, or a specific error string
      for division-by-zero or invalid operation.
    """
    op = operation.strip().lower()

    if op == 'add':
        return float(num1 + num2)
    elif op == 'subtract':
        return float(num1 - num2)
    elif op == 'multiply':
        return float(num1 * num2)
    elif op == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return float(num1 / num2)
    else:
        return "Error: Invalid operation '{}'.".format(operation)
