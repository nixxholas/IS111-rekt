def get_strings_with_digits(str_list, t):
    # Define a traversing index and a digit counter
    index, count = 0, 0
    # Loop the str_list
    while index < len(str_list):
        # if we've hit the digit threshold, immediately return the list till the traversing index.
        if count > t:
            return str_list[:index]
        # Else continue tabulating the count of digits in the current string of the index.
        else:
            # I mean, we have other ways to do this but who won't want a primitive one-liner?
            count += sum(ch.isdigit() for ch in str_list[index])
            index += 1

    # Return original ofc, lil shit is giving wrong data
    return str_list


# Cover all edge cases
print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn'], 5))
print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn'], 10))
print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn'], 6))


def get_strings_with_digits(str_list, t):
    digit_count = 0
    for i in range(len(str_list)):
        for ch in str_list[i]:
            if ch.isdigit():
                digit_count += 1

                if digit_count > t:
                    return str_list[:i + 1]

    # Return original ofc, lil shit is giving wrong data
    return str_list
