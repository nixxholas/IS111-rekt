import string

def find_second_letter(my_str):
    counted = False
    for i in range(len(my_str)):
        if my_str[i] in string.ascii_letters and counted:
            return i
        elif my_str[i] in string.ascii_letters and not counted:
            counted = True
    return -1
