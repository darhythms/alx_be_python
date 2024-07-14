from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"The date after {days} days will be: {formatted_future_date}")

def main():
    display_current_datetime()
    
    try:
        days = int(input("Enter the number of days: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
