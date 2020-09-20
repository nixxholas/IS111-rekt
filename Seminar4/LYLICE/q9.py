import string


def encode(sentence, n):
    characters = list(sentence)

    for i in range(0, len(characters)):
        if characters[i] in string.ascii_letters:  # If c is part of the ASCII letters, ROT(n) it
            ascii_index = string.ascii_letters.find(characters[i])  # Obtain the index of c in letter_dict

            if ascii_index + n > len(string.ascii_letters) - 1:  # If we exceed the length of ascii_letters
                # We need to reset from 0.
                ascii_index -= len(string.ascii_letters)

            characters[i] = string.ascii_letters[ascii_index + n]  # ROT(n) set

    return "".join(characters)


print(encode("Your mother dieZ", 1))
