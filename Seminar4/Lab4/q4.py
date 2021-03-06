def encrypt(msg):
    res = ''
    for char in msg:  # One liner .replace will not work, since we have overlapping replacements.
        res += 'e' if char == 'a' else 'i' if char == 'e' else 'o' if char == 'i' else 'u' if char == 'o' else 'a' \
            if char == 'u' else char
    return res


def encrypt_v2(msg):
    res = ''
    for char in msg:  # One liner .replace will not work, since we have overlapping replacements.
        res += 'e' if char == 'a' else 'i' if char == 'e' else 'o' if char == 'i' else 'u' if char == 'o' else 'a' \
            if char == 'u' else char
    return res[::-1]


print("The encrypted message is '" + encrypt_v2(input("What's the original message? ")) + "'")
