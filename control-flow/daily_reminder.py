# Step 1: Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with an unknown priority"

# Modify message if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Step 3: Provide Customized Reminder
print("\nReminder:", reminder)
