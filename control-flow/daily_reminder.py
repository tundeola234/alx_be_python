task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time = str(input("Is it time-bound? (yes/no): "))

match (priority, time):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!.")
    case ("high", "no"):
        print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case ("medium", "yes"):
        print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
    case ("medium", "no"):
        print(f"Reminder: '{task}' is a medium priority task. Try to complete it soon.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is a low priority task that is time-bound. Please address it today.")
    case ("low", "no"):
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input for priority or time-bound status.")