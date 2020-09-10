import string

alphabets = list(string.ascii_lowercase + string.ascii_uppercase)


def input_str(val):
    longest = ''
    current = ''
    for char in val:
        if char in alphabets:
            current += char
        else:
            longest = current if len(current) > len(longest) else longest
            current = ''  # Reset

    return longest


print(input_str(input("What's le string bro:")))
