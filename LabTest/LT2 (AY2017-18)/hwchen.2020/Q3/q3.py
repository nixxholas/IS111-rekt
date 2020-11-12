def get_postal_codes(file_name):
    res = []
    with open(file_name) as document:
        for line in document:
            details = line.strip().split(',')
            res.append((details[0], details[2][len(details[2]) - 7:]))
    return res

