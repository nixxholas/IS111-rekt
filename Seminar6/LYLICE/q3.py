# def print_expanded(n, res=''):
#     print(str(n) + ' + ' + res) if n % 10 <= 0 else print_expanded(n % 10, str(n - n % 10) + ' + ' + res)

def print_expanded(n):
    digits = list(str(n))
    res = ''

    for i in range(0, len(digits)):
        if int(digits[i]) > 0:
            res += (str(digits[i]) if (len(digits) - 1) == i else str(digits[i]) +
                                                                  ('0' * (len(digits) - (1 + i))) + ' + ')
    print(res)


print_expanded(100003)
