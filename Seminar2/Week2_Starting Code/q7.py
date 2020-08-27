# This line of code prompts the user for a system time.
try:
    input_str = float(input('Please enter the system time (in seconds): '))
except Exception:
    print("Bro, don't fool around with numbers.")

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0

# Put your code below

while input_str >= 86400:
    input_str -= 86400
    num_days += 1

while input_str >= 3600:
    input_str -= 3600
    num_hours += 1

while input_str >= 60:
    input_str -= 60
    num_minutes += 1

while input_str > 0:
    num_seconds = input_str
    input_str = 0


################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes)
      + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')