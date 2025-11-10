
# pattern_drawing.py
# Draw a square pattern of asterisks using a while loop and a nested for loop

def main():
    # Prompt user and validate input
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    # Use a while loop for rows
    row = 0
    while row < size:
        # Nested for loop to print stars on the same line
        for col in range(size):
            print("*", end="")   # print star without newline
        print()                  # newline after finishing the row
        row += 1

if __name__ == "__main__":
    main()

