# control-flow/daily_reminder.py

# 1. Prompt for a Single Task
task = input("Enter your task: ")

# Define the standard urgent phrase
immediate_action_phrase = "that requires immediate attention today!"

# Initialize priority validation loop variables
valid_priority = False
priority = ""

# Use a while loop to ensure we get a valid priority input
while not valid_priority:
    priority = input("Priority (high/medium/low): ").lower()
    
    if priority in ["high", "medium", "low"]:
        valid_priority = True
    else:
        # User entered an invalid priority, loop continues
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# 2. Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the final message variable
reminder_message = ""

# 3. Process the Task Based on Priority using Match Case

match priority:
    case "high":
        # Base message for High Priority
        reminder_message = f"Reminder: '{task}' is a high priority task"
        
        # Nested IF statement to check time sensitivity
        if time_bound == "yes":
            reminder_message += f" {immediate_action_phrase}"
        else:
            reminder_message += ". It is important and should be prioritized soon."

    case "medium":
        # Base message for Medium Priority
        reminder_message = f"Heads up: '{task}' is a medium priority task"
        
        # Nested IF statement to check time sensitivity
        if time_bound == "yes":
            reminder_message += f" {immediate_action_phrase}"
        else:
            reminder_message += ". Aim to complete it later this week."

    case "low":
        # Base message for Low Priority
        reminder_message = f"Note: '{task}' is a low priority task."
        
        # Nested IF statement to check time sensitivity
        if time_bound == "yes":
            # Urgency applied even to low priority if it's time-bound
            reminder_message = f"⚠️ WARNING: '{task}' is low priority but {immediate_action_phrase}"
        else:
            # Matches the requested example for low, non-time-bound tasks
            reminder_message += " Consider completing it when you have free time."

    # This wildcard case is a robust fallback, although the loop should prevent it from being reached
    case _:
        reminder_message = "Error: Invalid priority processing occurred."

# 4. Output the Customized Reminder
print("\n" + reminder_message)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")