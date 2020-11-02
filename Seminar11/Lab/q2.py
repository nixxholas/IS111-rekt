## Q2 Prime Numbers
# write your code below
def create_prime_dict(arr):
    res = {}
    for val in arr:
        res[val] = val <= 3 or (val > 3 and val % 2 != 0)

    return res
