#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.
def generate_child(num_list_str):
    res = []

    return res

# End of your additional functions.

def convert_to_list(num_list_str):
    res = []
    num_list_str = num_list_str[1:len(num_list_str) - 1]

    # Always loop till we clear the string
    while len(num_list_str) > 0:
        # Take the first item first
        cur_item = num_list_str.split(',')[0]

        # If it's just the value already
        if cur_item.isnumeric():
            # Easy game
            res.append(cur_item)
            # Update the string
            num_list_str = num_list_str[len(cur_item) + 1:]
        # Else it's a list...
        else:
            res.append(generate_child(num_list_str))

    return res

