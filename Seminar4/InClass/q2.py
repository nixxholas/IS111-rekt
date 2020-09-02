def display_numbers(m, n):
    """
    The function takes in two parameters: m and n. It is assumed that both m and n are integers,
    and m is less than or equal to n. The function displays all the integers between m and n (both inclusive) one by
    one, separated by spaces. However, the function handles the following numbers in a special way:
•	If the number is a multiple of 3 but not a multiple of 5, the function displays a hyphen instead of the number.
•	If the number is a multiple of 5 but not a multiple of 3, the function displays an asterisk instead of the number.
•	If the number is a multiple of both 3 and 5, the function displays a # instead of the number.
    """
    for i in range(m, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("#", end=' ')
        elif (i % 3 == 0) and (i % 5 != 0):
            print("-", end=' ')
        elif (i % 5 == 0) and (i % 3 != 0):
            print("*", end=' ')
        else:
            print(i, end=' ')


display_numbers(int(input("Enter the smaller number: ")), int(input("Enter the larger number: ")))
