# daily_reminder.py
# Single-task daily reminder using match/case, if, and loops for validation.
# Requires Python 3.10+ for match/case.

def get_nonempty_task(prompt="Enter your task: "):
    """Prompt until user types a non-empty task description."""
    while True:
        task = input(prompt).strip()
        if task:
            return task
        print("Task cannot be empty. Please describe your task.")

def get_valid_priority():
    """Prompt until user enters high, medium, or low (case-insensitive)."""
    valid = {"high", "medium", "low"}
    while True:
        pr = input("Priority (high/medium/low): ").strip().lower()
        if pr in valid:
            return pr
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def get_yes_no(prompt="Is it time-bound? (yes/no): "):
    """Prompt until user enters yes or no (case-insensitive)."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"yes", "no"}:
            return ans
        print("Please answer 'yes' or 'no'.")

def main():
    # 1) Get inputs
    task = get_nonempty_task("Enter your task: ")
    priority = get_valid_priority()
    time_bound = get_yes_no("Is it time-bound? (yes/no): ")

    # 2) Build the base reminder using match/case
    match priority:
        case "high":
            base = f"'{task}' is a high priority task"
        case "medium":
            base = f"'{task}' is a medium priority task"
        case "low":
            base = f"'{task}' is a low priority task"
        case _:
            # Should not happen because we validated, but keep a fallback.
            base = f"'{task}' has an unspecified priority"

    # 3) Modify based on time sensitivity using if
    if time_bound == "yes":
        # Time-sensitive tasks need immediate attention
        reminder = f"Reminder: {base} that requires immediate attention today!"
    else:
        # Non-time-sensitive -- suggest when convenient
        reminder = f"Note: {base}. Consider completing it when you have free time."

    # 4) Print the reminder
    print()
    print(reminder)

if __name__ == "__main__":
    main()
