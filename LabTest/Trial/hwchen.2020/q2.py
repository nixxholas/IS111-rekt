# =====
# q2.py
# =====
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def display_strings(str_list, ch):
    max_length = 0

    # Find the longest
    for phrase in str_list:
        if len(phrase) > max_length:
            max_length = len(phrase)

    # Set the '-'
    for i in range(len(str_list)):
        if len(str_list[i]) < max_length:
            str_list[i] += (ch * (max_length - len(str_list[i])))

    # Print the strings
    height = len(str_list) - 1
    while len(str_list) > 0:
        print((' ' * height) + str_list.pop(0))
        height -= 1

    return
