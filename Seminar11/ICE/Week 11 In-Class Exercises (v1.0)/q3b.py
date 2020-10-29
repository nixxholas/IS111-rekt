def read_into_dict(input_file):
    res = {}
    with open(input_file) as f:
        for line in f:
            cols = line.rstrip().split('\t')
            res[cols[0]] = cols[1]
    return res


print(read_into_dict('test.txt'))
