### Q2a: Universities 
# Write your code below:
def get_universities_founded_before(file_name, year):
    file = open(file_name, 'r')
    res = []

    for line in file:
        uni_datum = line.rstrip().split('\t')

        if int(uni_datum[2]) < year:
            res.append(uni_datum[0])

    return res

