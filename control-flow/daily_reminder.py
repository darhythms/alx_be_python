task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no) ")

time_1 = "that requires immediate attention today!"
time_2 = "Consider completing it when you have free time."
message_1 = "Note:"
message_2 = "Reminder:"
message_3 = "is a high priority task"
message_4 = "is a medium priority task"
message_5 = "is a low priority task"
sorry = "Sorry, you have to put a time"

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{message_2} '{task}' {message_3} {time_1}")
        elif time_bound == "no":
            print(f"{message_1} '{task}' {message_3}. {time_2}")
        else:
            print(sorry)
    case "medium":
        if time_bound == "yes":
            print(f"{message_2} '{task}' {message_4} {time_1}")
        elif time_bound == "no":
            print(f"{message_1} '{task}' {message_4}. {time_2}")
        else:
            print(sorry)
    case "low":
        if time_bound == "yes":
            print(f"{message_2} '{task}' {message_5} {time_1}")
        elif time_bound == "no":
            print(f"{message_1} '{task}' {message_5}. {time_2}")
        else:
            print(sorry)
