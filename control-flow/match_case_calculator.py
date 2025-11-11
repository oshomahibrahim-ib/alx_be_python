# Objective: Learn to use Match Case statements for handling multiple operations
# in a simple calculator program.

# 1. Prompt for User Input and convert to float for calculation
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Initialize result variable
result = None
output_message = ""

# 2. Perform the Calculation Using Match Case
match operation:
    case "+":
        result = num1 + num2
        output_message = f"The result is {result}."
    
    case "-":
        result = num1 - num2
        output_message = f"The result is {result}."
        
    case "*":
        result = num1 * num2
        output_message = f"The result is {result}."
        
    case "/":
        # Handle division by zero case gracefully
        if num2 == 0:
            output_message = "Cannot divide by zero."
        else:
            result = num1 / num2
            output_message = f"The result is {result}."
            
    # Handle cases where the user inputs an unexpected operation
    case _:
        output_message = "Invalid operation chosen. Please use +, -, *, or /."


# 3. Output the Result
print(output_message)