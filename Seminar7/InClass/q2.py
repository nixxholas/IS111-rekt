import string

def transform_string(sentence):
    chars = list(sentence)

    for i in range(len(chars)):
        if chars[i] in string.ascii_uppercase:
            chars[i] = 'L'
        elif chars[i] in string.ascii_lowercase:
            chars[i] = 'l'
        elif chars[i] in string.digits:
            chars[i] = 'd'
        else:
            chars[i] = 's'

    return "".join(chars)

