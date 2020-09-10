# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')


# Write your code below:
user_info = get_user_info()
if user_info[2] >= 60:
    print(("Mr. " if user_info[1] == 'M' else "Ms. ") + user_info[0] + ", you can get concessionary fare for senior "
                                                                       "citizens.")
elif user_info[2] <= 6:
    print(user_info[0] + ", you can get travel for free.")
elif user_info[3]:
    print("Mr. " if user_info[1] == 'M' else "Ms. " + user_info[0] + ", you can get concessionary fare for students.")
else:
    print("Mr. " if user_info[1] == 'M' else "Ms. " + user_info[0] + ", you need to pay full fare.")
