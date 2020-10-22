### Q2b: Universities 
# Write your code below:
def get_average_num_students(file_name):
    file = open(file_name, 'r')

    headcount = 0
    school_count = 0
    for line in file:
        uni_datum = line.rstrip().split('\t')
        school_count += 1
        headcount += int(uni_datum[3])

    # Return the xbar
    return headcount/school_count