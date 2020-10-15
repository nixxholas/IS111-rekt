import string


def is_pangram_old(sentence):
    chars = list(string.ascii_letters)

    for c in sentence:  # cup
        if c in chars:  # cCuUpP (from chars)
            chars.remove(c.upper())
            chars.remove(c.lower())

    return len(chars) == 0


def is_pangram(sentence):
    return len(set(string.ascii_lowercase) - set(sentence.lower())) == 0

