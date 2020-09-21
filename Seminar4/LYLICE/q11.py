def print_calendar(num_days, first_sun):
    print("Su Mo Tu We Th Fr Sa")
    if 0 > first_sun > 7:
        print("Invalid first sunday.")
        exit()

    # Attempt to obtain the first saturday in order to build a vertical checker to tell the subsequent code
    # when to stop printing the last item in each row
    first_sat = first_sun - 1
    # This will store all saturdays in the month.
    saturdays = []
    # Define a dynamic variable to stash the saturdays
    curr_sat = first_sat
    # While the curr_sat is less than the number of days in the month
    while curr_sat < num_days:
        # It means we have more saturday dates to add.
        saturdays.append(curr_sat)
        curr_sat += 7

    curr_day = 1
    while curr_day < num_days + 1:
        if curr_day < first_sun:  # if we're printing the first line in question.
            # We have to custom make this function to check how many blanks we need.
            # Let's say first_sun = 2, we only need to print once.
            days_to_print = first_sun - 1  # Defines the number of days I need to print out a number (day date).
            for dtp in range(7, 0, -1):  # Iterate the first week of days.
                if dtp <= days_to_print:  # If the current day counting backwards is less than or equal to days_to_print
                    print(' ' + str(curr_day), end=' ')  # We have to print the date/day out.
                    curr_day += 1  # Increment the curr_day we're at.
                else: print('  ', end=' ')  # Else, we have not reached yet.
            print()  # We're done with the first week of the month, we'll never touch this code again.
        else:
            if curr_day in saturdays:  # If the curr_day falls within one of the saturdays,
                # It is correct to imply that this is the last date of the line, we can now break line and move to the
                # next.
                print(' ' + str(curr_day)) if (curr_day < 10) else print(curr_day)
            else:  # Else we're still not at the end yet, just keep printing on the same line.
                print(' ' + str(curr_day), end=' ') if (curr_day < 10) else print(curr_day, end=' ')
            # Increment curr_day
            curr_day += 1


# TODO: Idk
def print_calendar_v2(num_days, first_sun):
    print("Su Mo Tu We Th Fr Sa")
    if 0 > first_sun > 7:
        print("Invalid first sunday.")
        exit()

    days_in_week = [[], [], [], [], [], [], []]
    month_arr = []

    day_ptr = 0
    # while day_ptr < num_days + 1:
    #     if

    if first_sun > 1:
        day_ptr = first_sun - 1
        for curr_day in range(first_sun - 1, 0, -1):
            days_in_week[day_ptr].append(curr_day)
            day_ptr = (day_ptr - 1) if (day_ptr - 1 >= 0) else 6

    day_ptr = 0  # Pointer day, set to 0 since 0 = sunday
    for curr_day in range(first_sun, num_days + 1):
        # Add the current day in the tuple collection
        # days_in_week[0][2].append(str(curr_day) if curr_day < 10 else ' ' + str(curr_day))
        days_in_week[day_ptr].append(curr_day)
        day_ptr = (day_ptr + 1) if day_ptr + 1 < len(days_in_week) else 0

    # print(days_in_week)


print_calendar_v2(30, 7)
