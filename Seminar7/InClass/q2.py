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


def transform_string_jun(sentence):
    # create lists to add the replaced chars
    upper_chars = []
    lower_chars = []
    digit_chars = []
    symbol_chars = []

    sentence = list(sentence)
    for i in range(len(sentence)):
        if sentence[i] in string.ascii_uppercase:
            upper_chars.append(sentence[i])
            sentence[i] = 'L'
        elif sentence[i] in string.ascii_lowercase:
            lower_chars.append(sentence[i])
            sentence[i] = 'l'
        elif sentence[i] in string.digits:
            digit_chars.append(sentence[i])
            sentence[i] = 'd'
        else:
            symbol_chars.append(sentence[i])
            sentence[i] = 's'

    # print num of each grp of characters
    print('Number of uppercase letters: ', len(upper_chars))
    print('Number of lowercase letters: ', len(lower_chars))
    print('Number of digits: ', len(digit_chars))
    print('Number of symbols: ', len(symbol_chars))

    # return the replaced string
    return "".join(sentence)
