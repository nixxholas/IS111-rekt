# =====
# q1a.py
# =====
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def add_first_odd_digits(str_list):
    odd_digits = ['1', '3', '5', '7', '9']
    val = 0
    for word in str_list:
        chars = list(word)

        while len(chars) > 0:
            c = chars.pop(0)

            if c in odd_digits:
                val += int(c)
                chars = []

    return val
