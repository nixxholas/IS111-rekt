def count_long_strings(str_list):
    res = []
    for item in str_list:
        if len(item) >= 5:
            res.append(item)
    return len(res)
