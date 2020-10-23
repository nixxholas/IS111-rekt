### Q5a: Matrix

# Write your code below:
def get_matrix(file_name):
    file = open(file_name, 'r')
    res = []

    for line in file:
        row = []
        cells = line.rstrip().split(' ')

        for cell in cells:
            row.append(float(cell))

        res.append(row)

    return res
