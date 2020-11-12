#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

import copy

# If needed, you can define your own additional functions here.
# Start of your additional functions.
def str_list_traversal(num_list_str, parent=False):
    res = []

    cur_val = ''
    while len(num_list_str) > 0:
        if num_list_str[0] == '[':
            res.append(str_list_traversal(num_list_str[1:]))
            # Slice the string and take out the length of the current res - the whitespaces
            num_list_str = num_list_str[len(str(res[len(res) - 1])) - (len(res[len(res) - 1]) - 1):]
        elif num_list_str[0] == ']':
            if cur_val.isnumeric():
                res.append(int(cur_val))
            cur_val, num_list_str = '', num_list_str[1:]
            return res
        elif num_list_str[0] == ',':
            if cur_val.isnumeric():
                res.append(int(cur_val))
            cur_val, num_list_str = '', num_list_str[1:]
        else:
            cur_val += copy.deepcopy(num_list_str[0])
            num_list_str = num_list_str[1:]

    return res[0] if parent else res
# End of your additional functions.

def convert_to_list(num_list_str):
    res = str_list_traversal(num_list_str, True)

    return res

