def compute_sum(m, n):
    sum = 0
    for i in range(m, n + 1):
        sum += i
    return sum


my_sum = compute_sum(4, 10)
print("The sum is " + str(my_sum))
