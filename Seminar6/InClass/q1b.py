def merge_list(list1, list2):
    res = []

    longest = len(list1) if len(list1) > len(list2) else len(list2)
    for i in range(longest):
        if i < len(list1):
            res.append(list1[i])
        if i < len(list2):
            res.append(list2[i])

    return res


print(merge_list([1, 3, 10, 15, 4, 7, 12], [9, 5, 2]))
