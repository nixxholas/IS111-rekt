def get_sum_of_odd_numbers(num_list):
    sum = 0
    for num in num_list:
        if num % 2 != 0:
            sum += num
    return sum
