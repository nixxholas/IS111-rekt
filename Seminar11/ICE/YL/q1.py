# write your answer here
def has_same_value(d1, d2, key):
    return True if (key in d1.keys() and key in d2.keys()) and (d1[key] == d2[key]) else False
