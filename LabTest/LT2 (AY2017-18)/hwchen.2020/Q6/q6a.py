def scramble(word, file_name):
    res = []
    common_words = []
    with open(file_name) as document:
        for line in document:
            common_words.append(line.rstrip())

    for common_word in common_words:
        if is_similar(word, common_word):
            res.append(common_word)
    return res


def is_similar(word, other_word):
    word_chars = list(word)
    other_word_chars = list(other_word)
    if len(word_chars) == 0 or len(other_word_chars) == 0 or len(word_chars) != len(other_word_chars):
        return False

    for c in word_chars:
        if c in other_word_chars:
            other_word_chars.remove(c)

    return len(other_word_chars) == 0
