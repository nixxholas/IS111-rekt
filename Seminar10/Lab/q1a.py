## Q1 Reading Files
# Write your code below:
##############################

def print_alternate_lines(file_name):
    file = open(file_name, 'r')

    is_odd_line = True
    for line in file:
        if is_odd_line:
            print(line.rstrip())
            is_odd_line = False
        else:
            is_odd_line = True
