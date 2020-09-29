import string

def is_pangram(sentence):
    chars = set(string.ascii_letters)

    for c in sentence:
        if c in chars:
            chars.remove(c.upper())
            chars.remove(c.lower())

    return len(chars) == 0

