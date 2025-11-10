# match_case_calculator.py
# Simple calculator demonstrating match/case (Python 3.10+)

def main():
    # 1) Prompt user for input
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")
    operator = input("Choose the operation (+, -, *, /): ")

    # 2) Convert inputs to floats with validation
    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except ValueError:
        print("Invalid number entered. Please enter valid numeric values.")
        return

    # 3) Perform operation using match/case
    match operator:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation selected. Choose one of +, -, *, /.")

if __name__ == "__main__":
    main()
