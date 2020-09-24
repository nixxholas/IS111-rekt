# Name: Nicholas Chen
# Email ID: hwchen.2020

def add_even_numbers(str_list):
    res = 0
    for s in str_list:
        # Split the strings first
        num_strings = s.split('|')
        # Then loop the numbers and find even numbers to find the result.
        for num_string in num_strings:
            if int(num_string) % 2 == 0: res += int(num_string)

    return res