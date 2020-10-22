### Q1b Reading Files
# Write your code below:
def print_alternate_columns(file_name):
    file = open(file_name, 'r')

    for line in file:
        columns = line.rstrip().split('&')

        line_content = ''
        for i in range(0, len(columns), 2):
            line_content += columns[i] + '&'
        print(line_content[:-1])
