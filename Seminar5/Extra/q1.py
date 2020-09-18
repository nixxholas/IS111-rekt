def reverse_words(sentence):
    words = sentence.split(' ')

    for i in range(0, len(words)):
        if len(words[i]) > 0:
            words[i] = words[i][::-1]  # Flip in a simple way

    return " ".join(words)


print(reverse_words("Python is a programming language."))