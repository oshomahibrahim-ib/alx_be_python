# multiplication_table.py
# Program to generate a multiplication table for a given number using a for loop

# Prompt the user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
