# Name: Nicholas Chen
# Email ID: hwchen.2020

def get_number_of_long_strings(str_list, n):
    count = 0
    for s in str_list:
        if len(s) > n: count += 1
    return count
