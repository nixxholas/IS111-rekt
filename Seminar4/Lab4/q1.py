month = int(input("Enter month: "))
days_in_months = [30, 28, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]

if month - 1 < -1 or month > len(days_in_months):
    print("Enter a number between 1 and 12 only!")
else:
    print("There are", days_in_months[month - 1], "days in this month.")