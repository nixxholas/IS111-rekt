def convert_to_dict(tuples):
    res = {}
    for t in tuples:
        res[t[0]] = t[1]
    return res


def convert_to_dict_v2(tuples):
    return dict(tuples)