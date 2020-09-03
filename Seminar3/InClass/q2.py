def get_day_of_week(day):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(day, "Invalid day of week.")


def get_day_of_week_alt(day):
    if day < 0: return "Your number should be at least 0."
    days_in_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if len(days_in_week) <= day: return "Your number should be at most 6."
    return days_in_week[day]


print(get_day_of_week(int(input("What day number is it? "))))
print(get_day_of_week_alt(int(input("Enter a number indicating the day of a week [0 to 6]: "))))