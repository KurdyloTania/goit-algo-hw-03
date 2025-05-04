from datetime import datetime

def get_days_from_today(date):
    try:
        date_string = datetime.strptime(date, "%Y-%m-%d").date()
        now = datetime.now().date()
        days_difference = now - date_string
        number_of_days = days_difference.days
        return number_of_days
    except ValueError:
        print("Error! Please enter the date in the format \"YYYY-MM-DD\"!\n")
        return None

while True:      
    user_input = input("Enter date in \"YYYY-MM-DD\" format: ")

    count_days = get_days_from_today(user_input)
    if count_days != None:
        print(f"Number of days from a given date to the current one: {count_days}")
        break