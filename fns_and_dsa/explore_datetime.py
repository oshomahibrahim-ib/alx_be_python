# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get current date/time and print it in 'YYYY-MM-DD HH:MM:SS' format.
    Saves the datetime in a variable named `current_date`.
    """
    current_date = datetime.now()  # current_date variable as required
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate the future date after adding days_to_add days to now.
    Saves the result in a variable named `future_date` (a date object).
    Returns that date object.
    """
    # Use datetime.now() so calculation is based on the current moment
    current_date = datetime.now()
    future_datetime = current_date + timedelta(days=days_to_add)
    # Save the date portion in future_date as requested (YYYY-MM-DD)
    future_date = future_datetime.date()
    return future_date

def main():
    # Part 1: display current datetime
    current_date = display_current_datetime()  # current_date is returned (and was defined inside function)

    # Part 2: prompt user for integer days and calculate future date
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer number of days (e.g. 10).")

    future_date = calculate_future_date(days)  # future_date variable as required
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
