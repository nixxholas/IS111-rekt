#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#
def count_names_with_space(name_list):
    count = 0
    for name in name_list:
        count += 1 if len(name.split(' ')) > 1 else 0
    return count
