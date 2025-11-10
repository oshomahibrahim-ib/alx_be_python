# Objective: Create a simplified Python script that uses conditional statements, Match Case,
# and loops to remind the user about a single, priority task for the day based on time sensitivity.

# 1. Prompt for a Single Task (Standard Input)
task = input("Enter your task: ")

# Initialize variables
priority = ""
is_time_bound = ""
reminder_message = ""
# Define the phrase for immediate action
immediate_action_phrase = "that requires immediate attention today!"

# Use a while loop to ensure we get a valid priority input (demonstrating loop control)
valid_priority = False
while not valid_priority:
    priority = input("Priority (high/medium/low): ").lower()
    
    if priority in ["high", "medium", "low"]:
        valid_priority = True
    else:
        # Prompt for invalid input
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# 2. Prompt for time sensitivity
is_time_bound = input("Is it time-bound? (yes/no): ").lower()

# 3. Process the Task Based on Priority using Match Case
# The match/case structure determines the base message format.

match priority:
    case "high":
        # High priority tasks always get a strong base message
        reminder_message = f"Reminder: '{task}' is a high priority task"
        
        # Use an if statement to modify the reminder based on time sensitivity
        if is_time_bound == "yes":
            # Append the urgent phrase if time-bound
            reminder_message += f" {immediate_action_phrase}"
        else:
            # Custom message if high but not explicitly time-bound
            reminder_message += ". It is important and should be prioritized soon."

    case "medium":
        # Medium priority tasks are secondary
        reminder_message = f"Heads up: '{task}' is a medium priority task"
        
        # Use an if statement to modify the reminder based on time sensitivity
        if is_time_bound == "yes":
            # Append the urgent phrase if time-bound
            reminder_message += f" {immediate_action_phrase}"
        else:
            reminder_message += ". Aim to complete it later this week."

    case "low":
        # Low priority tasks are flexible
        reminder_message = f"Note: '{task}' is a low priority task."
        
        # Use an if statement to modify the reminder based on time sensitivity
        if is_time_bound == "yes":
            # Even low priority can be urgent if time-bound
            reminder_message = f"⚠️ WARNING: '{task}' is low priority but {immediate_action_phrase}"
        else:
            # The requested message for low, non-time-bound tasks
            reminder_message += " Consider completing it when you have free time."

    # This case handles any scenario where the priority variable somehow avoids the validation loop 
    # and is not one of the expected values, making the script robust.
    case _:
        reminder_message = "Error: Invalid priority processing occurred."

# 4. Output the Customized Reminder
print("\n" + reminder_message)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")