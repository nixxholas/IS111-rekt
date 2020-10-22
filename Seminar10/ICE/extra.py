# Define a function called get_strings_with_digits() that takes in two parameters:
# (1) A list of strings called str_list. (2) An integer value t.
#
# The function returns a list that contains any n strings in str_list such that the total number of digits in these
# n strings is strictly larger than t. The function should find the smallest n that satisfies the condition above
# and return those n strings. If the total number of digits in all the strings in str_list is still not larger than t,
# then the function returns a list that contains all the strings in str_list.
#
# Example: str_list is ['ab123', '99', 'X7Z', 'k', 'lmn‘, 'IS111'], and t is 5, then the function should
# return ['ab123', 'IS111']. 
def get_strings_with_digits(str_list, t):
    str_list = insertionSort(str_list)
    res = []

    # Insertion sort first
    return str_list


print(get_strings_with_digits(['ab123', '99', 'X7Z', 'k', 'lmn', 'IS111'], 5))