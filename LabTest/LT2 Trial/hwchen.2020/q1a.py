import string

def find_last_letter(my_str):
    for i in range(len(my_str) - 1, -1, -1):
        if my_str[i] in string.ascii_letters:
            return i
    return -1
