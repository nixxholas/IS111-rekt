def check_numbers(list1, list2):
    divisible = True
    for i in list1:
        i_divisible = False
        for j in list2:
            if i % j == 0:
                i_divisible = True
                break

        if not i_divisible: return i_divisible

    return divisible


print(check_numbers([3, 8, 10, 15, 16], [9, 3, 2, 5]))
print(check_numbers([3, 8, 10, 6, 2, 5], [9, 3, 7]))

