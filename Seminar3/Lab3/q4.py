## Q4
# PART 1
# The following function is for you to implement.
def get_ticket_info(age):
    # Modify the code below to return the right value
    return (15, True) if (age >= 60) else (33, False) if (age >= 13) else (22, True)


# ################################################################################
# The code below is to test your implementation of the function above. 
# DO NOT MODIFY THE CODE BELOW!

# The following line of code should display (33, False)
print(get_ticket_info(40))

# The following line of code should display (22, True)
print(get_ticket_info(10))

# PART 2
# Write your code below to prompt the user for age
# and print the expected output
age = int(input("How old are you? "))
t_info = get_ticket_info(age)
if t_info[1]: print("Congratulations! You qualify for a discount.")
print("You need to pay $" + str(t_info[0]))
